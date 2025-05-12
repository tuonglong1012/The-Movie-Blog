from pydantic import BaseModel
from typing import Optional

class ReviewOut(BaseModel): 
    id: int
    username: str
    movie_detail_id: Optional[int]
    show_reviews: Optional[str]
    hidden_reviews: Optional[str] 
    
    class Config:
        from_attributes: True 

class ReviewCreate(BaseModel):
    user_id: int
    movie_id: int
    content: str
    class Config:
        from_attributes: True 
