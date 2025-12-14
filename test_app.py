import pytest
from app import app

@pytest.fixture
def client():
    # Tworzymy klienta testowego naszej aplikacji
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Sprawdza, czy strona główna działa i zwraca poprawny tekst"""
    response = client.get('/')
    
    # Test 1: Czy kod odpowiedzi to 200 (OK)?
    assert response.status_code == 200
    
    # Test 2: Czy w treści jest słowo "Witaj"?
    # (używamy b"" bo Flask zwraca bajty)
    assert b"Witaj" in response.data