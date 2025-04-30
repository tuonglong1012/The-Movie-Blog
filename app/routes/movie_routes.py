from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers.movie_controller import import_movies
from ..database import get_db

router = APIRouter()

@router.post("/import-json")
def import_from_json(db: Session = Depends(get_db)):
    return import_movies(db)
