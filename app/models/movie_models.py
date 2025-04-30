from sqlalchemy import Column, Integer, String, Text, ARRAY, TIMESTAMP, Float
from ..database import Base

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(Integer)
    title = Column(String(255))
    score = Column(Float)
    rank = Column(Integer)
    episodes = Column(Integer)
    aired = Column(String(100))
    type = Column(String(50))  
    members = Column(String(50))
