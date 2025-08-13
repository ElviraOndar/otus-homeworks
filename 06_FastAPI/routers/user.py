from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserCreate


def create_user(db: Session, user: UserCreate) -> User:
    """
    Создаёт нового пользователя в базе данных.

    Параметры:
        db (Session): Активная сессия SQLAlchemy.
        user (UserCreate): Pydantic-схема с данными для нового пользователя.

    Логика работы:
        1. Создаёт новый ORM-объект User на основе данных из user.
        2. Добавляет объект в сессию и сохраняет изменения в базе.
        3. Обновляет объект из базы, чтобы получить сгенерированные поля (например, id).

    Возвращает:
        ORM-объект созданного пользователя.
    """
    new_user = User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user