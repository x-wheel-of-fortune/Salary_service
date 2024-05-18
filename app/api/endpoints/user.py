from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.crud import user as user_crud
from app.api.schemas.user import UserCreate
from app.db.sessions import get_db

router = APIRouter()

# This endpoint is intended for demonstration purposes only.
# In an actual project the process of creating and managing users
# would be more complex.
@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = user_crud.get_user(db, username=user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    user_crud.create_user(db, username=user_data.username,
                          password=user_data.password,
                          salary=user_data.salary,
                          promotion_date=user_data.promotion_date)
    return {"detail": "User created successfully"}
