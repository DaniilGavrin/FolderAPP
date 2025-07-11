import os
import uvicorn
import pytest
import sys
import time
import multiprocessing

# Переключаемся в директорию проекта
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from app.app import app
# Функция запуска сервера (выполняется в отдельном процессе)
def run_server():
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

# Основная функция
def main():
    print("🔄 Запуск тестов...")

    # Сначала запускаем тесты
    result = pytest.main(["tests/", "-v", "-p", "no:warnings"])

    if result != pytest.ExitCode.OK:
        print("❌ Тесты провалены. Сервер не запущен.")
        sys.exit(1)

    print("✅ Все тесты пройдены. Запуск сервера...")

    # Запуск сервера в отдельном процессе
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()

    try:
        # Ждём завершения работы процесса (например, при Ctrl+C)
        server_process.join()
    except KeyboardInterrupt:
        print("🛑 Остановка сервера...")
        server_process.terminate()
        server_process.join()
        sys.exit(0)

if __name__ == "__main__":
    main()