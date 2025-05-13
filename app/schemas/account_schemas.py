from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    date_of_birth: str
    password: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True


class ChangeUserPassword(BaseModel):
    username: str
    old_password: str
    new_password: str

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    id: int
    username: str
    date_of_birth: str
    status: bool
    role: int

    class Config:
        from_attributes = True
