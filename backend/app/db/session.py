import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Absolute path to project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)

DB_PATH = os.path.join(PROJECT_ROOT, "data", "db", "roadrunner.db")

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("DB PATH =", DB_PATH)
