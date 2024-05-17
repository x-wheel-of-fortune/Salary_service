from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.crud import user as user_crud
from app.api.schemas.token import Token
from app.api.schemas.user import UserLogin
from app.core.security import create_access_token
from app.db.sessions import get_db

router = APIRouter()


@router.post("/login", response_model=Token)
def login_for_access_token(user_data: UserLogin,
                           db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, username=user_data.username,
                                       password=user_data.password)
    if not user:
        raise HTTPException(status_code=401,
                            detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
