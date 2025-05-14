import scrapy
from scrapy.crawler import CrawlerProcess
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.account_models import UserModel
from ..schemas.account_schemas import UserCreate, UserOut
import json
import os
import datetime

router = APIRouter()


def create_user(user: UserCreate, db: Session):
    # Check if user exists
    existing_user = (
        db.query(UserModel).filter(UserModel.username == user.username).first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Create new user
    new_user = UserModel(
        username=user.username,
        date_of_birth=datetime.datetime.strptime(user.date_of_birth, "%Y-%m-%d").date(),
        password=user.password,
        status=True,  # mặc định
        role=0,  # mặc định
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session):
    return db.query(UserModel).all()


def banned_user(user_id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.status = False
    db.commit()
    db.refresh(user)
    return user

def unlock_user(user_id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.status = True
    db.commit()
    db.refresh(user)
    return user

def update_role(user_id: int, new_role: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not new_role:
        raise HTTPException(
            status_code=404, detail="Role must be 0 (user) or 1 (admin)"
        )
    user.role = new_role
    db.commit()
    db.refresh(user)
    return user


def delete_user(user_id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": f"User with ID {user_id} has been deleted"}


def login_user(username: str, password: str, db: Session):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password != password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    if not user.status:
        raise HTTPException(status_code=403, detail="User not approved")
    return user


def change_password(username: int, old_password: str, new_password: str, db: Session):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password == old_password:
        user.password = new_password
    else:
        raise HTTPException(status_code=400, detail="Old password is incorrect")
    db.commit()
    db.refresh(user)
    return {"message": f"Change password success"}
