import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bonjour" in response.data

def test_api_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200

def test_metrics(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"app_requests_total" in response.data