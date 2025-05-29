import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.session import base


@pytest.fixture
def session():
    """Эта функция 1) создает временную БД для тестов,
    2) создает все таблицы на основе моих моделей,
    3) создает новую сессию,
    4) передает текущую сессию в тесты при помощи yield,
    4) закрывает сессию"""
    engine = create_engine("sqlite:///:memory:")
    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


