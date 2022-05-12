import pytest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"data_wrangling"))
import sqlalchemy as sa

from data_wrangling.data_wrangling import create_app
from data_wrangling.blueprints.auth.models import Users
from data_wrangling.db.db import db

TEST_DB_NAME = 'data_wrangling_test'
TEST_DB_USER = 'test_user'
TEST_DB_PASSWORD = 'test_password'
TEST_DB_URL = f'postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@localhost:5432/{TEST_DB_NAME}'

@pytest.fixture
def test_user():
    test_user = Users(name='stacy', email='stacy@email.com', password='password')
    return test_user

@pytest.fixture
def test_user_bad_password():
    test_user_bad_password = Users(name='stacy', email='stacy@email.com', password='123456')
    return test_user_bad_password

@pytest.fixture
def test_client(db_session):
    test_app = create_app()
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URL
    db.app = test_app
    db.session = db_session

    with test_app.test_client() as test_client:
        with test_app.app_context():
            db.create_all()
        yield test_client

@pytest.fixture(scope="session")
def engine():
    return sa.create_engine(TEST_DB_URL)


@pytest.fixture(scope="session")
def tables(engine):
    Users.metadata.create_all(engine)
    yield
    Users.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine,tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = sa.orm.Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()