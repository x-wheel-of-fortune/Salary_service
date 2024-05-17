import datetime

from sqlalchemy.orm import Session

from app.app.api.models.user import User
from app.app.core.security import get_password_hash, verify_password


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def create_user(db: Session, username: str, password: str,
                salary: int, promotion_date: datetime.datetime):
    hashed_password = get_password_hash(password)
    user = User(username=username,
                hashed_password=hashed_password,
                salary=salary, promotion_date=promotion_date)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_salary(db: Session, username: str):
    user = get_user(db, username)
    if not user:
        return None
    return {"salary": user.salary, "promotion_date": user.promotion_date}
