from flask import url_for
import psycopg

from data_wrangling.blueprints.auth.models import Users


def test_signup_new_user(test_client, test_user, db_session):
    # new user is not already in db
    query = db_session.query(Users)
    new_user = query.filter(Users.email == test_user.email)
    new_user_exists_in_db = new_user.one_or_none()
    assert not new_user_exists_in_db
    
    # send signup POST request
    user_input_data = {
        'email': test_user.email,
        'name': test_user.name,
        'password': test_user.password
    }
    resp = test_client.post('/auth/signup', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    # after signup, redirect to login page
    assert resp.request.path == url_for('auth.login')

    # after signup, new user is in db
    new_user_after_post = query.filter(Users.email == test_user.email)
    new_user_exists_in_db_after_post = new_user_after_post.one_or_none()
    assert new_user_exists_in_db_after_post

def test_signup_existing_user(test_client, test_user, db_session):
    # existing user is already in db
    query = db_session.query(Users)
    existing_user = query.filter(Users.email == test_user.email)
    existing_user_exists_in_db = existing_user.one_or_none()
    assert existing_user_exists_in_db

    # send signup POST request
    user_input_data = {
        'email': test_user.email,
        'name': test_user.name,
        'password': test_user.password
    }
    resp = test_client.post('/auth/signup', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    
    # if the user already exists, stay on signup page and flash error message
    assert resp.request.path == url_for('auth.signup')
    assert b'a user with that email address already exists' in resp.data

def test_login_existing_user(test_client, test_user, db_session):
    # existing user is already in db
    query = db_session.query(Users)
    existing_user = query.filter(Users.email == test_user.email)
    existing_user_exists_in_db = existing_user.one_or_none()
    assert existing_user_exists_in_db
    
    # send login POST request
    user_input_data = {
        'email': test_user.email,
        'name': test_user.name,
        'password': test_user.password
    }
    resp = test_client.post('/auth/login', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    
    # after login, redirect to profile page
    assert resp.request.path == url_for('main.profile')
    assert bytes(test_user.name, 'utf-8') in resp.data

def test_login_existing_user_bad_password(test_client, test_user_bad_password, db_session):
    # existing user is already in db
    query = db_session.query(Users)
    existing_user = query.filter(Users.email == test_user_bad_password.email)
    existing_user_exists_in_db = existing_user.one_or_none()
    assert existing_user_exists_in_db

    # send login POST request
    user_input_data = {
        'email': test_user_bad_password.email,
        'name': test_user_bad_password.name,
        'password': test_user_bad_password.password
    }
    resp = test_client.post('/auth/login', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200

    # if password is incorrect, stay on login page and flash error message
    assert resp.request.path == url_for('auth.login')
    assert b'please check your login details and try again.' in resp.data