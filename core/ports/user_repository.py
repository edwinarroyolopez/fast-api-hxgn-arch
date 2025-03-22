from abc import ABC, abstractmethod
from core.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> User:
        pass