from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from config import DATABASE_URL
from typing import Generator

# Движок
engine = create_engine(DATABASE_URL)

# Базовый класс
Base = declarative_base()

# Фабрика сессий
SessionLocal = sessionmaker(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



