from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.account_schemas import UserCreate, UserOut, UserLogin, ChangeUserPassword
from ..controllers.account_controller import create_user, get_user, approve_user, update_role, delete_user, login_user, change_password
import requests
from typing import List

router = APIRouter()


@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)


@router.get("/user/user-list", response_model=list[UserOut])
def get_list_user(db: Session = Depends(get_db)):
    return get_user(db)


@router.post("/user/banned/{user_id}", response_model=UserOut)
def approve(user_id: int, db: Session = Depends(get_db)):
    return approve_user(user_id, db)


@router.put("/user/{user_id}/role/{new_role}", response_model=UserOut)
def change_user_role(user_id: int, new_role: int, db: Session = Depends(get_db)):
    return update_role(user_id, new_role, db)


@router.delete("/user/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)


@router.post("/user/login", response_model=UserOut)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user.username, user.password, db)


@router.put("/user/{user_id}/Change_password")
def change_user_password(user: ChangeUserPassword, db: Session = Depends(get_db)):
    return change_password(user.username, user.old_password, user.new_password, db)
