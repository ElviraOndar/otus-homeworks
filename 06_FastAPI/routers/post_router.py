from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.post_schema import PostCreate, PostRead
from crud.post_crud import create_post, get_post, update_post, delete_post
from models.tag import Tag

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostRead)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает POST-запрос, когда клиент хочет добавить новый пост.

    Данная функция:
    1) принимает post (PostCreate) - Pydantic-схему с данными нового поста,
    2) принимает db (Session) - активную сессию SQLAlchemy,
    3) проверяет, что введенные теги для поста существуют в базе данных; если нет, вызывает HTTPException,
    4) вызывает функцию create_post из CRUD, чтобы создать ORM-объект нового поста и сохранить его в базе данных,
    5) возвращает ответ клиенту.

    Функция возвращает ORM-объект, но FastAPI благодаря response_model преобразует его в Pydantic-схему PostRead,
    которая содержит данные созданного поста - название, контент, дату, автора, теги, ID поста.
    """
    requested_tag_ids = set(post.tags)  # убираем возможные дубликаты ID тегов
    db_tags = db.query(Tag).filter(Tag.id.in_(requested_tag_ids)).all()  # возвращает список найденных тегов

    if len(db_tags) != len(requested_tag_ids):
        raise HTTPException(status_code=400, detail="Один или несколько тегов не существуют")

    return create_post(db=db, post=post)


@router.get("/{post_id}", response_model=PostRead)
def get_post_endpoint(post_id: int, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает GET-запрос: получить один пост по его ID.

    1) Ищет пост в базе данных с помощью функции get_post из CRUD.
    2) Если пост не найден, вызывает 404.
    3) Возвращает найденный пост в виде Pydantic-схемы PostRead.
    """
    db_post = get_post(db=db, post_id=post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Пост не найден")
    return db_post


@router.put("/{post_id}", response_model=PostRead)
def update_post_endpoint(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает PUT-запрос: обновить существующий пост по ID.

    1) Проверяет, что все теги, указанные в post.tags, существуют.
    2) Вызывает update_post из CRUD.
    3) Если пост не найден, вызывает 404.
    4) Возвращает обновленный пост в виде Pydantic-модели PostRead, чтобы отправить клиенту.
    """
    requested_tag_ids = set(post.tags)
    db_tags = db.query(Tag).filter(Tag.id.in_(requested_tag_ids)).all()

    if len(db_tags) != len(requested_tag_ids):
        raise HTTPException(status_code=400, detail="Один или несколько тегов не существуют")

    updated_post = update_post(db=db, post_id=post_id, post_data=post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Пост не найден")

    return updated_post


@router.delete("/{post_id}")
def delete_post_endpoint(post_id: int, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает DELETE-запрос: удалить пост по ID.

    1) Вызывает функцию delete_post из CRUD.
    2) Если пост не найден, вызывает 404.
    3) Если успешно, возвращает {"ok": True}.
    """
    success = delete_post(db=db, post_id=post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Пост не найден")
    return {"ok": True}


