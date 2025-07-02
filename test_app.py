import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads properly"""
    rv = client.get('/')
    assert rv.status_code == 200

@patch('app.get_response')
def test_chat_endpoint(mock_get_response, client):
    """Test the chat endpoint"""
    # Configure the mock to return a predefined response
    mock_get_response.return_value = "Hello! How can I assist you?"
    
    response = client.post('/chat', 
                         json={'message': 'Hello'})
    assert response.status_code == 200
    assert 'response' in response.get_json()
    assert response.get_json()['response'] == "Hello! How can I assist you?" 