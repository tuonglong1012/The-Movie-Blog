
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers.movie_controller import import_movies, create_user
from ..database import get_db
from ..controllers.movie_controller import get_movie
from ..schemas.movie_schemas import MovieOut, User
from ..controllers.movie_controller import get_all_movies
import requests

router = APIRouter()

# [post]/api/import-json


@router.post("/import-json")
def import_from_json(db: Session = Depends(get_db)):
    return import_movies(db)

# [post]/api/fetch-json


@router.post("/fetch-json")
def fetch_import(db: Session = Depends(get_db)):
    get_movie()
    response = requests.post("http://localhost:8000/api/import-json")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail="Lỗi khi import vào DB")

    return {
        "crawl": "Hoàn tất crawling",
        "import": response.json()
    }


# [get]/api/movies
@router.get("/movies", response_model=list[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return get_all_movies(db)


@router.post("/signup", response_model=User)
def signup(user: User, db: Session = Depends(get_db)):
    return create_user(user, db)
