import scrapy
from scrapy.crawler import CrawlerProcess
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.reviews_models import MovieReview
from ..models.movie_models import MovieDetail
from ..models.account_models import UserModel

from ..schemas.review_schemas import ReviewCreate 

import json
import os

router = APIRouter()




# Hàm thêm review theo id user
def create_review(review: ReviewCreate, db: Session):
    get_username = db.query(UserModel).filter(UserModel.id == review.user_id).first()
    if not get_username:
        raise HTTPException(status_code=404, detail="User not found")
    # Kiểm tra phim đã tồn tại chưa
    existing_movie = db.query(MovieDetail).filter(MovieDetail.id == review.movie_id).first()
    if not existing_movie:
        raise HTTPException(status_code=400, detail="Movie is not existing")
    new_review = MovieReview(
        user_id = review.user_id,
        movie_detail_id = review.movie_id,
        username = get_username.username,
        show_reviews = review.content,
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
# Hàm lấy review theo id phim
def get_review_by_id(db: Session, id: int):
    return db.query(MovieReview).filter(MovieReview.movie_detail_id == id).all()
# Hàm xóa review
def delete_review(db: Session, review_id: int):
    review = db.query(MovieReview).filter(MovieReview.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(review)
    db.commit()
    return {"message": f"Review with ID {review_id} has been deleted"}