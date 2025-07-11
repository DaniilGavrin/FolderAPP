# app.py
from fastapi import FastAPI
from .routes import router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("✅ Сервер успешно запущен")

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 Сервер остановлен")

# Подключение маршрутов
app.include_router(router)