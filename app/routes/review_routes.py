from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.review_schemas import ReviewOut,ReviewCreate
from ..controllers.review_controller import get_review_by_id,create_review,delete_review
import requests
from typing import List

router = APIRouter()


# [GET]/api/review/{id}/review-by-movie
@router.get("/review/{id}/review-by-movie", response_model=List[ReviewOut])
def get_review(id: int, db: Session = Depends(get_db)):
    review = get_review_by_id(db, id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review
@router.get("/review/{id}/review-by-user", response_model=List[ReviewOut])
def get_review_by_user(id: int, db: Session = Depends(get_db)):
    review_user = get_review_by_id(db, id)
    if review_user is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review_user
# [POST]/api/review/{id}/review-by-user
@router.post("/review/create/{id}", response_model=ReviewOut)
def get_review(review: ReviewCreate, db: Session = Depends(get_db)):
    review = create_review(review,db)
    return review
# [DELETE]/api/review/{id}/delete-review
@router.delete("/review/{id}/delete-review")
def remove_review(review_id: int, db: Session = Depends(get_db)):
    review = delete_review(db,review_id)
    return review