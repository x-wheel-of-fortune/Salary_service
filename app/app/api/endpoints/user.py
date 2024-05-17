from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.app.api.crud import user as user_crud
from app.app.api.schemas.user import UserCreate
from app.app.db.sessions import get_db

router = APIRouter()


@router.post("/user")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = user_crud.get_user(db, username=user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    user = user_crud.create_user(db, username=user_data.username,
                                 password=user_data.password,
                                 salary=user_data.salary,
                                 promotion_date=user_data.promotion_date)
    return user
