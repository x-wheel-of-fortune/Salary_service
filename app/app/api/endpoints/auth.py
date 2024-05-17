from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.api.schemas.token import Token
from app.app.api.schemas.user import UserLogin
from app.app.api.crud import user as user_crud
from app.app.db.sessions import get_db
from app.app.core.security import create_access_token

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(user_data: UserLogin, db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, username=user_data.username, password=user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
