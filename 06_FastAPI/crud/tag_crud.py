from sqlalchemy.orm import Session
from models.tag import Tag
from schemas.tag_schema import TagCreate


def create_tag(db: Session, tag: TagCreate) -> Tag:
    """
    Эта функция создает новый тег в базе данных.
    Она принимает tag (TagCreate) - Pydantic-схему с данными для нового тега - его названием.

    Функция возвращает ORM-объект созданного тега.
    """
    new_tag = Tag(name=tag.name)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


def get_tag(db: Session, tag_id: int) -> Tag | None:
    """
    Эта функция получает тег по его ID.
    Она принимает tag_id (int) - ID тега.
    Функция возвращает ORM-объект найденного тега или None, если тег не найден.
    """
    return db.query(Tag).filter(Tag.id == tag_id).first()


def get_tags(db: Session, skip: int = 0, limit: int = 100) -> list[Tag]:
    """
    Эта функция получает из базы данных список тегов.
    Она принимает:
    1) skip (int, optional) - количество тегов, которые нужно пропустить от начала выборки (по умолчанию - 0).
    2) limit (int, optional) - максимальное количество возвращаемых тегов (по умолчанию - 100).

    Функция возвращает list[Tag] - список ORM-объектов тегов.
    """
    return db.query(Tag).offset(skip).limit(limit).all()


def update_tag(db: Session, tag_id: int, new_tag: TagCreate) -> Tag | None:
    """
    Эта функция обновляет данные существующего тега.
    Она принимает:
    1) tag_id (int) - ID тега, который нужно обновить.
    2) new_tag (TagCreate) - Pydantic-схему, которая валидирует новые данные для тега - новое название.

    Функция возвращает обновленный ORM-объект тега или None, если тег не был найден.
    """
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    tag.name = new_tag.name
    db.commit()
    db.refresh(tag)
    return tag


def delete_tag(db: Session, tag_id: int) -> bool:
    """
    Эта функция удаляет тег по его ID.
    Она принимает tag_id (int) - ID тега, который надо удалить.
    Функция возвращает True, если удаление прошло успешно, False - если тег не был найден.
    """
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    db.delete(tag)
    db.commit()
    return True


