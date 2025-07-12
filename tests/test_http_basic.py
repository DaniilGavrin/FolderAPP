# tests/test_app.py
from fastapi.testclient import TestClient

from app import data
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


"""
Возвращает список проектов
"""
def test_get_projects_valid_key():
    response = client.post("/project", json={"key": data.KEY_USER})
    assert response.status_code == 200 or response.status_code == 204

def test_get_projects_invalid_key():
    response = client.post("/project", json={"key": "wrong_key"})
    assert response.status_code == 403
    assert response.json() == {"detail": "❌ Неверный API-ключ"}

def test_get_projects_no_projects():
    response = client.post("/project", json={"key": data.KEY_USER})
    assert response.status_code == 204
    assert response.text == ""