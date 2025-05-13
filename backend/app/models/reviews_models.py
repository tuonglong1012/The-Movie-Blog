from sqlalchemy import Column, Integer, String, Text, ARRAY, TIMESTAMP, Float, Boolean,ForeignKey
from ..database import Base

class MovieReview(Base):
    __tablename__ = 'movies_reviews'

    id = Column(Integer, primary_key=True)
    movie_detail_id = Column(Integer, nullable=False)
    username = Column(String)
    show_reviews = Column(String)  
    hidden_reviews = Column(String)  
    user_id = Column(Integer, ForeignKey("account.id"), nullable=False)
