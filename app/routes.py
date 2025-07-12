# routes.py
from fastapi import APIRouter, HTTPException, Body

from app import data
from app.database import Database

router = APIRouter()

# Подключение к БД
db = Database()

@router.get("/")
def read_root():
    return {"message": "Hello World"}

@router.get("/check")
def check():
    return {"message": "Client OK"}

"""
Мы должны на сервере принять ключ, сверить с ключом из файла,
и вернуть в ответ список проектов или отказ из-за ключа или код ответа если проектов нет не 404 а другой нужный  
"""
@router.post("/project")
def get_projects(request: dict = Body(...)):
    """
    Принимает GET-запрос с ключом в теле:
    {
        "key": "my_secret_key_123"
    }
    """
    client_key = request.get("key")

    if not client_key:
        raise HTTPException(status_code=400, detail="🔑 Ключ не предоставлен")

    if client_key != data.KEY_USER:
        raise HTTPException(status_code=403, detail="❌ Неверный API-ключ")

    projects = db.get_table_project()
    if not projects:
        raise HTTPException(status_code=204, detail="🚫 Проекты отсутствуют")

    return {
        "projects": [
            {"id": pid, "name": name, "description": desc}
            for pid, name, desc in projects
        ]
    }