import pytest
from flask.testing import FlaskClient


@pytest.fixture('module')
def token():
    return __name__ + ':token'


def test_get_token(client: FlaskClient, token, request):
    res = client.get('/token')
    assert res.status_code == 200
    token_ = res.json
    request.config.cache.set(token, token_)


def test_secure_page(client: FlaskClient, token, request):
    token_ = request.config.cache.get(token, None)
    res = client.post('/secure', json={})
    assert res.status_code == 401
    res = client.post('/secure', json={'token': token_})
    assert res.status_code == 200
