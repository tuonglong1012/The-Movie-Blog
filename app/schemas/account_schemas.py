from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    age: Optional[int]
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    age: int
    status: bool
    role: int
    class Config:
        from_attributes = True