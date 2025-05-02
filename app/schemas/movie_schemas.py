from pydantic import BaseModel
from typing import Optional


class MovieOut(BaseModel):
    id: int
    title: Optional[str]
    score: Optional[float]
    rank: Optional[int]
    episodes: Optional[int]
    external_id: Optional[int]
    type: Optional[str]
    aired: Optional[str]
    members: Optional[str]

    class Config:
        from_attributes: True


class MovieDetailOut(BaseModel):
    id: int
    title: str
    score: Optional[float]
    rank: Optional[int]
    status: Optional[str]
    episodes: Optional[int]
    synopsis: Optional[str]
    link: Optional[str]
    synonyms: Optional[str]
    japanese: Optional[str]
    type: Optional[str]
    aired: Optional[str]
    premiered: Optional[str]
    broadcast: Optional[str]
    producers: Optional[str]
    licensors: Optional[str]
    studios: Optional[str]
    source: Optional[str]
    genres: Optional[str]
    demographic: Optional[str]
    duration: Optional[str]
    rating: Optional[str]
    popularity: Optional[str]
    members: Optional[str]
    favorites: Optional[str]
    external_id: Optional[int]

    class Config:
        # Điều này cho phép FastAPI chuyển đổi dữ liệu từ model SQLAlchemy sang schema Pydantic
        from_attributes: True


class MovieIn(BaseModel):
    title: str
    score: Optional[float]
    rank: Optional[int]
    status: Optional[str]
    episodes: Optional[int]
    synopsis: Optional[str]
    link: Optional[str]
    synonyms: Optional[str]
    japanese: Optional[str]
    type: Optional[str]
    aired: Optional[str]
    premiered: Optional[str]
    broadcast: Optional[str]
    producers: Optional[str]
    licensors: Optional[str]
    studios: Optional[str]
    source: Optional[str]
    genres: Optional[str]
    demographic: Optional[str]
    duration: Optional[str]
    rating: Optional[str]
    popularity: Optional[str]
    members: Optional[str]
    favorites: Optional[str]
    external_id: Optional[int]

    class Config:
        # Điều này cho phép FastAPI chuyển đổi dữ liệu từ model SQLAlchemy sang schema Pydantic
        from_attributes: True


class CharacterOut(BaseModel):
    id: int
    name: str
    role: Optional[str]
    link: Optional[str]
    voice_actor: Optional[str]
    voice_actor_link: Optional[str]
    voice_actor_country: Optional[str]

    class Config:
        from_attributes: True


class MovieOut(BaseModel):
    id: int
    title: Optional[str]
    score: Optional[float]
    rank: Optional[int]
    episodes: Optional[int]
    external_id: Optional[int]
    type: Optional[str]
    aired: Optional[str]
    members: Optional[str]

    class Config:
        from_attributes: True


class FavoriteCreate(BaseModel):
    user_id: int
    movie_id: int


class FavoriteOut(BaseModel):
    id: int
    user_id: int
    movie_id: int

    class Config:
        from_attributes = True
