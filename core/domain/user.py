# En core/domain/user.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None  # <-- Campo opcional
    username: str
    password_hash: str

    class Config:
        from_attributes = True