from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from app.models import Base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

database_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(engine)

with engine.connect() as connection:
    print("Database connection successful!")