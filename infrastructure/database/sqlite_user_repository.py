import sqlite3
from core.domain.user import User
from core.ports.user_repository import UserRepository

class SQLiteUserRepository(UserRepository):
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection
        self._init_table()  # <-- Esto crea la tabla

    def _init_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        self.conn.commit()


    def save(self, user: User) -> User:
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO users (username, password_hash) VALUES (?, ?)',  # <-- Paréntesis corregido
            (user.username, user.password_hash),
        )
        self.conn.commit()
        user.id = cursor.lastrowid
        return user

    def find_by_username(self, username: str) -> User:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        return User(**row) if row else None