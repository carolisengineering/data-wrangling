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
