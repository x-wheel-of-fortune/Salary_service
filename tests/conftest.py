import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Determine the absolute path to the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Set the environment variable for the test environment file
env_file_path = os.path.join(project_root, 'tests/.env')
os.environ["ENV_FILE"] = env_file_path

from app.main import app
from app.db.base import Base
from app.core.config import settings

# Use the test database URL
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,
                                   bind=engine)


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
