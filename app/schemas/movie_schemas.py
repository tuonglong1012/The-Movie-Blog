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
        from_attributes = True
