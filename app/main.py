from fastapi import FastAPI

from app.api.endpoints import auth, salary, user
# Create tables in the database if they don't exist
from app.api.models import user as UserModel
from app.db.sessions import engine

UserModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers for authentication and salary endpoints
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(salary.router, tags=["salary"])
app.include_router(user.router, tags=["user"])
