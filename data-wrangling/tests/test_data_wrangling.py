from data_wrangling import __version__
#from data_wrangling import main


def test_version():
    assert __version__ == '0.1.0'

def test_index(test_client):
    resp = test_client.get('/')
    assert resp.status_code == 200
    assert resp.text == 'Index'

def test_profile(test_client):
    resp = test_client.get('/profile')
    assert resp.status_code == 200
    assert resp.text == 'Profile'

def test_login(test_client):
    resp = test_client.get('/login')
    assert resp.status_code == 200
    assert resp.text == 'Login'

def test_signup(test_client):
    resp = test_client.get('/signup')
    assert resp.status_code == 200
    assert resp.text == 'Signup'

def test_logout(test_client):
    resp = test_client.get('/logout')
    assert resp.status_code == 200
    assert resp.text == 'Logout'
