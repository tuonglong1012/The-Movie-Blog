from sqlalchemy import Column, Integer, String, Text, ARRAY, TIMESTAMP, Float, Boolean
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
    type = Column(String(50))
    members = Column(String(50))


class MovieDetail(Base):
    __tablename__ = 'movies_detail'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, nullable=False)
    title = Column(String(255))
    score = Column(Float)
    rank = Column(Integer)
    status = Column(String)
    episodes = Column(Integer)
    synopsis = Column(Text)  # Mảng có thể chuyển sang chuỗi JSON nếu cần
    link = Column(String)
    synonyms = Column(String)
    japanese = Column(String)
    type = Column(String)
    aired = Column(String)
    premiered = Column(String)
    broadcast = Column(String)
    producers = Column(String)
    licensors = Column(String)
    studios = Column(String)
    source = Column(String)
    genres = Column(String)
    demographic = Column(String)
    duration = Column(String)
    rating = Column(String)
    popularity = Column(String)
    members = Column(String)
    favorites = Column(String)


class Character(Base):
    __tablename__ = 'movies_characters'

    id = Column(Integer, primary_key=True)
    movie_detail_id = Column(Integer, nullable=False)
    name = Column(String)
    role = Column(String)
    link = Column(String)
    voice_actor = Column(String)
    voice_actor_link = Column(String)
    voice_actor_country = Column(String)


class MovieReview(Base):
    __tablename__ = 'movies_reviews'

    id = Column(Integer, primary_key=True)
    movie_detail_id = Column(Integer, nullable=False)
    username = Column(String)
    show_reviews = Column(ARRAY(String))  # Dùng ARRAY cho mảng chuỗi
    hidden_reviews = Column(ARRAY(String))  # Dùng ARRAY cho mảng chuỗi


class UserModel(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    age = Column(Integer)
    password = Column(String, nullable=False)
    status = Column(Boolean, default=False)
