from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserCreate


def create_user(db: Session, user: UserCreate) -> User:
    """
    Эта функция создает нового пользователя в базе данных.
    Она принимает:
    1) db (Session) - активная сессия SQLAlchemy,
    2) user (UserCreate) - Pydantic-схема с данными для нового пользователя - его именем.

    Затем функция:
    1) создает новый ORM-объект User с именем, которое ввел клиент через Pydantic-схему.
    2) добавляет объект в сессию и сохраняет изменения в базе.
    3) обновляет объект из базы, чтобы получить сгенерированные поля (например, id).

    Функция возвращает ORM-объект созданного пользователя. В роутере мы преобразуем его в Pydantic-схему,
    чтобы вернуть клиенту
    """
    new_user = User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int) -> User | None:
    """
    Эта функция получает из базы данных конкретного пользователя по его ID.
    Она принимает user_id (int) - ID пользователя.
    Функция возвращает ORM-объект пользователя, либо None, если пользователь не найден.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """
    Эта функция получает список пользователей из базы данных.
    Она принимает:
    1) skip (int) - количество записей, которые нужно пропустить (по умолчанию - 0).
    2) limit (int) - максимальное количество записей, которое нужно вернуть (по умолчанию 100).

    Функция возвращает список ORM-объектов пользователей.
    """
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_data: UserCreate) -> User | None:
    """
    Эта функция обновляет данные пользователя по его ID.
    Она принимает:
    1) user_id (int) - ID пользователя.
    2) user_data (UserCreate) - Pydantic-схема с новыми данными пользователя - именем.

    Функция возвращает обновленный ORM-объект пользователя, либо None, если пользователь не найден.
    """
    user = db.query(User).filter(User.id == user_id).first()
    user.name = user_data.name
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    """
    Эта функция удаляет пользователя из базы данных по его ID.
    Она принимает user_id (int) - ID пользователя.

    Функция возвращает True, если удаление прошло успешно, иначе - False.
    """
    user = db.query(User).filter(User.id == user_id).first()

    db.delete(user)
    db.commit()
    return True
