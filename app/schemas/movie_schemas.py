from pydantic import BaseModel
from typing import List, Optional

class MovieCreate(BaseModel):
    title: str
    score: Optional[float]

class MovieOut(MovieCreate):
    id: int
    class Config:
        from_attributes  = True
