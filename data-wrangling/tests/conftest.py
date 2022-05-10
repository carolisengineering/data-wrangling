import pytest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"data_wrangling"))

from data_wrangling.data_wrangling import create_app
from data_wrangling.blueprints.auth.models import Users
from data_wrangling.db.db import db

TEST_DB_URL = 'postgresql://test_user:test_password@localhost:5432/data_wrangling_test'

@pytest.fixture
def test_user():
    test_user = Users(name='stacy', email='stacy@email.com', password='password')
    return test_user

@pytest.fixture
def test_client():
    test_app = create_app()
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URL
    db.app = test_app

    with test_app.test_client() as test_client:
        with test_app.app_context():
            db.create_all()
        yield test_client