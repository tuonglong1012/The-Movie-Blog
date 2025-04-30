from sqlalchemy import Column, Integer, String, Text, ARRAY, TIMESTAMP, Float
from ..database import Base

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(Integer)
    title = Column(String(255))
    score = Column(Float)
    rank = Column(Integer)
    status = Column(String(50))
    episodes = Column(Integer)
    synopsis = Column(ARRAY(Text))
    link = Column(Text)
    aired = Column(String(100))
    premiered = Column(String(100))
    broadcast = Column(String(100))
    source = Column(String(100))
    duration = Column(String(50))
    rating = Column(Text)
    popularity = Column(Integer)
    members = Column(Integer)
    favorites = Column(Integer)
    created_at = Column(TIMESTAMP)
    type = Column(String(50))  
