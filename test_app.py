import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads properly"""
    rv = client.get('/')
    assert rv.status_code == 200

def test_chat_endpoint(client):
    """Test the chat endpoint"""
    response = client.post('/chat', 
                         json={'message': 'Hello'})
    assert response.status_code == 200
    assert 'response' in response.get_json() 