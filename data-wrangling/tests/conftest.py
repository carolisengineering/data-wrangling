import pytest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"data_wrangling"))

from data_wrangling.data_wrangling import create_app
from db.db import db


@pytest.fixture
def test_client():
    test_app = create_app()
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    with test_app.test_client() as test_client:
        with test_app.app_context():
            db.create_all()
        yield test_client