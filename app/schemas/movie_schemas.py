from pydantic import BaseModel
from typing import Optional

class MovieCreate(BaseModel):
    title: str
    score: Optional[float] = None
    rank: Optional[int] = None
    episodes: Optional[int] = None
    external_id: Optional[int] = None
    type: Optional[str] = None
    aired: Optional[str] = None
    members: Optional[int] = None

class MovieOut(MovieCreate):
    id: int

    class Config:
        from_attributes = True  # (tương đương với orm_mode trong Pydantic V1)
