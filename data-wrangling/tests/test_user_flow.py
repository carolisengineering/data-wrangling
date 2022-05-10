from flask import url_for
import psycopg

def test_signup_new_user(test_client, test_user):
    # assert user is not already in db
    user_input_data = {
        'email': test_user.email,
        'name': test_user.name,
        'password': test_user.password
    }
    resp = test_client.post('/auth/signup', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    assert resp.request.path == url_for('auth.login')

def test_signup_existing_user(test_client, test_user):
    # need to assert test_user is already in db
    user_input_data = {
        'email': test_user.email,
        'name': test_user.name,
        'password': test_user.password
    }
    resp = test_client.post('/auth/signup', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    assert resp.request.path == url_for('auth.signup')
    # assert error message is in response

def test_login_existing_user(test_client, test_user):
    # assert user is already in db
    user_input_data = {
        'email': test_user.email,
        'name': test_user.name,
        'password': test_user.password
    }
    resp = test_client.post('/auth/login', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    assert resp.request.path == url_for('main.profile')

def test_login_existing_user_bad_password(test_client, test_user_bad_password):
    # assert user is already in db
    user_input_data = {
        'email': test_user_bad_password.email,
        'name': test_user_bad_password.name,
        'password': test_user_bad_password.password
    }
    resp = test_client.post('/auth/login', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    assert resp.request.path == url_for('auth.login')
    # assert error message is in response