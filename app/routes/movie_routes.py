from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.movie_schemas import MovieCreate, MovieOut
from ..controllers.movie_controller import create_movie
from ..database import get_db

router = APIRouter()

@router.post("/movies", response_model=MovieOut)
def create(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db, movie)
