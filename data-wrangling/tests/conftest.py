import os
import tempfile

import pytest
from data_wrangling import create_app, db


@pytest.fixture
def test_client():
    test_app = create_app()
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    with test_app.test_client() as test_client:
        with test_app.app_context():
            db.create_all()
        yield test_client