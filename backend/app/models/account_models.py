from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ARRAY,
    TIMESTAMP,
    Float,
    Boolean,
    Date,
)
from ..database import Base


class UserModel(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=False)
    password = Column(String, nullable=True)
    status = Column(Boolean, default=False)
    role = Column(Integer, default=0)
