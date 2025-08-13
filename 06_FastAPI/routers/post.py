from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.post_schema import PostCreate, PostRead
from crud.post_crud import create_post
from models.tag import Tag

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostRead)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает POST-запрос на префикс /posts, когда клиент хочет добавить новый пост.

    Данная функция:
    1) принимает post (PostCreate) - Pydantic-схему с данными нового поста,
    2) принимает db (Session) - активную сессию SQLAlchemy,
    3) проверяет, что введенные теги для поста существуют в базе данных; если нет, вызывает HTTPException,
    4) вызывает функцию create_post из CRUD, чтобы создать ORM-объект нового поста и сохранить его в базе данных,
    5) возвращает ответ клиенту.

    Функция возвращает ORM-объект, но FastAPI благодаря response_model преобразует его в Pydantic-схему PostRead,
    которая содержит данные созданного поста - название, контент, дату, автора, теги, ID поста.
    """
    requested_ids = set(post.tags)  # убираем возможные дубликаты ID тегов
    db_tags = db.query(Tag).filter(Tag.id.in_(requested_ids)).all()  # возвращает список найденных тегов

    if len(db_tags) != len(requested_ids):
        raise HTTPException(status_code=400, detail="Один или несколько тегов не существуют")

    return create_post(db=db, post=post)



