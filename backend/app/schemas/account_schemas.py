from pydantic import BaseModel
from typing import Optional
from datetime import date  # Thêm import cho kiểu date

class UserCreate(BaseModel):
    username: str
    date_of_birth: str  # Đây là kiểu string, bạn có thể để là string nếu muốn nhận giá trị dưới dạng chuỗi
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
    date_of_birth: date  # Đảm bảo đã import đúng kiểu `date`
    status: bool
    role: int

    class Config:
        from_attributes = True
