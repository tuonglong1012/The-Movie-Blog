from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from ..controllers.movie_controller import import_movies
from ..database import get_db
from ..controllers.movie_controller import get_movie 
from ..schemas.movie_schemas import MovieOut,MovieDetailOut,CharacterOut,ReviewOut
from ..controllers.movie_controller import get_all_movies,get_movie_by_id,get_character_by_id,get_review_by_id
import requests
from typing import List

router = APIRouter()

# [POST]/api/import-json
@router.post("/import-json")
def import_from_json(db: Session = Depends(get_db)):
    return import_movies(db)


# [post]/api/fetch-json
@router.post("/fetch-json")
def fetch_import(db: Session = Depends(get_db)):
    get_movie()
    response = requests.post("http://localhost:8000/api/import-json")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Lỗi khi import vào DB")
    return {
        "crawl": "Hoàn tất crawling",
        "import": response.json()
    }

# [GET]/api/movies
@router.get("/movies",response_model=list[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return get_all_movies(db)

# [GET]/api/movies/:id
@router.get("/movies/{id}", response_model=MovieDetailOut)
def detail_movie(id: int, db: Session = Depends(get_db)):
    movie = get_movie_by_id(db, id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
# [GET]/api/movies/:id/character
@router.get("/movie/{id}/character",response_model=List[CharacterOut])
def get_character(id: int, db: Session = Depends(get_db)):
    character = get_character_by_id(db,id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character
# [GET]/api/movies/:id/review
@router.get("/movie/{id}/review",response_model=List[ReviewOut])
def get_review(id: int, db: Session = Depends(get_db)):
    review = get_review_by_id(db,id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

# [get]/api/movies
@router.get("/movies", response_model=list[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return get_all_movies(db)


