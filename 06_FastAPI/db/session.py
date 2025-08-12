from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# Движок
engine = create_engine(DATABASE_URL)

# Базовый класс
Base = declarative_base()

# Фабрика сессий
SessionLocal = sessionmaker(bind=engine)


