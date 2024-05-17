from sqlalchemy import Column, Integer, String, DateTime

from app.app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    salary = Column(Integer)
    promotion_date = Column(DateTime)
