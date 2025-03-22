from infrastructure.web.api import app
import sqlite3
from infrastructure.database.sqlite_user_repository import SQLiteUserRepository

# Conexión a la base de datos PERSISTENTE (users.db)
DATABASE_URL = "users.db"
conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)

# Inicializar el repositorio (creará la tabla)
user_repository = SQLiteUserRepository(conn)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)