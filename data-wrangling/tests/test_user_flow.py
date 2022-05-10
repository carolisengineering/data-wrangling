from flask import url_for
import psycopg

def test_signup_new_user(test_client, test_user):
    user_input_data = {
        'email': test_user.email,
        'name': test_user.name,
        'password': test_user.password
    }
    resp = test_client.post('/auth/signup', data=user_input_data, follow_redirects=True)
    assert resp.status_code == 200
    assert resp.request.path == url_for('auth.login')