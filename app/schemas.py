from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None  # Optional

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True # This tells Pydantic to work with SQLAlchemy models
