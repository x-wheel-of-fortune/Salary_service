from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.app.api.crud import user as user_crud
from app.app.api.models.user import User
from app.app.api.schemas.user import UserSalary
from app.app.core.security import get_current_user
from app.app.db.sessions import get_db

router = APIRouter()


@router.get("/salary", response_model=UserSalary)
def get_user_salary(current_user: User = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    user_salary = user_crud.get_user_salary(db, username=current_user.username)
    if not user_salary:
        raise HTTPException(status_code=404, detail="User not found")
    return user_salary
