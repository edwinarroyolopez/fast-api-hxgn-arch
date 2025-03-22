from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from core.services.user_service import UserService
from infrastructure.database.sqlite_user_repository import SQLiteUserRepository
import sqlite3

app = FastAPI()

# Conexión global a la base de datos (para simplificar)
DATABASE_URL = "users.db"
conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)
conn.row_factory = sqlite3.Row

# Inicializar el repositorio (creará la tabla)
user_repository = SQLiteUserRepository(conn)
user_service = UserService(user_repository)

class UserRegister(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: UserRegister):
    try:
        registered_user = user_service.register_user(user.username, user.password)
        return {"message": "Usuario registrado exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
def login(user: UserRegister):
    try:
        logged_in_user = user_service.login_user(user.username, user.password)
        return {"message": "Inicio de sesión exitoso"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))