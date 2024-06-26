import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    salary: int
    promotion_date: datetime.datetime


class UserLogin(BaseModel):
    username: str
    password: str


class UserSalary(BaseModel):
    salary: int
    promotion_date: datetime.datetime


class Token(BaseModel):
    access_token: str
    token_type: str
