from data_wrangling import __version__

def test_version():
    assert __version__ == '0.1.1'

def test_index(test_client):
    resp = test_client.get('/')
    assert resp.status_code == 200
    assert b'data rodeo' in resp.data
    assert b'a place to wrangle data' in resp.data

def test_profile(test_client):
    resp = test_client.get('/profile')
    assert resp.status_code == 200
    assert b'welcome!' in resp.data

def test_login(test_client):
    resp = test_client.get('/auth/login')
    assert resp.status_code == 200
    assert b'login here' in resp.data

def test_signup(test_client):
    resp = test_client.get('/auth/signup')
    assert resp.status_code == 200
    assert b'sign up here' in resp.data

def test_logout(test_client):
    resp = test_client.get('/auth/logout')
    assert resp.status_code == 200
    assert resp.text == 'Logout'
