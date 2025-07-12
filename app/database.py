# database.py
import sqlite3
import os

class Database:
    def __init__(self, db_name="db.sqlite3"):
        self.db_name = db_name
        self.check_table()

    def _connect(self):
        """Создаёт новое подключение к БД"""
        return sqlite3.connect(self.db_name)

    def create_table_project(self):
        """Создаёт таблицу project."""
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS project (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )
            """)
            conn.commit()

    def check_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS project (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )
            """)
            conn.commit()

    def get_table_project(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, description FROM project")
            return cursor.fetchall()