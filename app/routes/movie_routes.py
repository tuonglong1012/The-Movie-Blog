from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers.movie_controller import import_movies
from ..database import get_db
from ..controllers.movie_controller import get_movie
from ..schemas.movie_schemas import MovieOut, MovieDetailOut, CharacterOut,FavoriteOut,FavoriteCreate
from ..controllers.movie_controller import get_all_movies, get_movie_by_id, get_character_by_id,add_favorite,get_favorites_by_user,delete_favorite
import requests
from typing import List

router = APIRouter()

# [POST]/api/import-json
@router.post("/import-json")
def import_from_json(db: Session = Depends(get_db)):
    return import_movies(db)

# [POST]/api/fetch-json
@router.post("/fetch-json")
def fetch_import(db: Session = Depends(get_db)):
    get_movie()
    response = requests.post("http://localhost:8000/api/import-json")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail="Lỗi khi import vào DB")

    return {
        "message": "Hoàn tất import",
        "import": response.json()
    }

# [GET]/api/movies
@router.get("/movies", response_model=list[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return get_all_movies(db)

# [GET]/api/movies/:id
@router.get("/movies/{id}/movie-detail", response_model=MovieDetailOut)
def detail_movie(id: int, db: Session = Depends(get_db)):
    movie = get_movie_by_id(db, id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# [GET]/api/movies/:id/character
@router.get("/movie/{id}/character", response_model=List[CharacterOut])
def get_character(id: int, db: Session = Depends(get_db)):
    character = get_character_by_id(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

# [GET]/api/movies
@router.get("/movies", response_model=list[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return get_all_movies(db)

# [POST]/api/movies/add-favorites-movies
@router.post("/movies/add-favorites-movies", response_model=FavoriteOut)
def add_favorite_movie(fav: FavoriteCreate, db: Session = Depends(get_db)):
    return add_favorite(fav,db)

# [GET]/api/movies/user/{user_id}/favorites-movies
@router.get("/movies/user/{user_id}/favorites-movies", response_model=list[FavoriteOut])
def get_favorites(user_id: int, db: Session = Depends(get_db)):
    return get_favorites_by_user(user_id,db)


@router.delete("/movies/remove-favorites-movies")
def remove_favorite(user_id: int, movie_id: int, db: Session = Depends(get_db)):
    return delete_favorite(user_id,movie_id,db)