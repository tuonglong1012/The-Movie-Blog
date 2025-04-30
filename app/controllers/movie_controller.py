from sqlalchemy.orm import Session
from ..models.movie_models import Movie
from ..schemas.movie_schemas import MovieCreate

def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
