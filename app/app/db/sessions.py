from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.app.core.config import settings

# Database URL for PostgreSQL
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL


# Create a SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class to manage database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
