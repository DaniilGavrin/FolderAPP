# tests/test_app.py
from fastapi.testclient import TestClient
from app.app import app  # Импорт из пакета app

client = TestClient(app)

def test_api():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_check():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"message": "Client OK"}