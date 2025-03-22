from core.ports.user_repository import UserRepository
from core.domain.user import User
import bcrypt

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, username: str, password: str) -> User:
        # Verificar si el usuario ya existe
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            raise ValueError("El nombre de usuario ya está en uso.")

        # Hashear la contraseña
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Crear el usuario
        user = User(id=None, username=username, password_hash=password_hash.decode('utf-8'))
        return self.user_repository.save(user)

    def login_user(self, username: str, password: str) -> User:
        user = self.user_repository.find_by_username(username)
        if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            raise ValueError("Nombre de usuario o contraseña incorrectos.")
        return user