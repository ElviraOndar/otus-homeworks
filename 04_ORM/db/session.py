from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# Движок
engine = create_engine(DATABASE_URL, echo=True)

# Базовый класс
base = declarative_base()

# Фабрика сессий
Session = sessionmaker(bind=engine)


