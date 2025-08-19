from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from models.post import Post
from models.tag import Tag
from schemas.post_schema import PostCreate


def create_post(db: Session, post: PostCreate):
    """Эта функция создает новый пост в базе данных.
    Она принимает аргументы:
    1) db (Session) - активная сессия SQLAlchemy для работы с БД.
    2) post (PostCreate) - Pydantic-схема с данными для нового поста.

    Затем функция: 1) создает новый ORM-объект Post,
    2) загружает из базы нужные теги по введенным ID,
    3) связывает теги с постом,
    4) сохраняет пост в базе и обновляет его в ORM-системе.

    Функция возвращает новый ORM-объект созданного поста.
    В роутере этот объект будет преобразован в Pydantic-схему, чтобы можно было вернуть его клиенту.
    """
    new_post = Post(
        title=post.title,
        content=post.content,
        datetime=post.datetime,
        user_id=post.user_id
    )

    # Находим теги по id
    tags = db.query(Tag).filter(Tag.id.in_(post.tags)).all()
    new_post.tags = tags

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_post(db: Session, post_id: int):
    """
    Эта функция получает из базы данных пост по его ID - сразу с данными об авторе и тегах поста.
.
    Функция использует:
    1) joinedload(Post.user) — чтобы сразу загрузить данные автора поста.
    2) joinedload(Post.tags) — чтобы сразу загрузить привязанные к посту теги.

    Функция возвращает ORM-объект поста в случае, если он был найден, либо None.
    Позднее в роутере мы преобразуем этот ORM-объект в Pydantic-схему, чтобы можно было вернуть клиенту.
    """
    return (
        db.query(Post)
        .options(
            joinedload(Post.user),
            joinedload(Post.tags)
        )
        .filter(Post.id == post_id)
        .first()
    )


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    """
    Эта функция получает список постов из базы данных с подгрузкой автора и тегов.
    Она принимает:
    - skip (int) — сколько записей пропустить,
    - limit (int) — сколько постов вернуть.

    Возвращает список ORM-объектов Post. В роутере мы преобразуем их в Pydantic-схему PostRead для возврата клиенту.
    """
    return (
        db.query(Post)
        .options(
            joinedload(Post.user),   # сразу подгружаем автора
            joinedload(Post.tags)    # сразу подгружаем теги
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_post(db: Session, post_id: int, post_data: PostCreate):
    """
    Эта функция обновляет существующий пост в базе данных по его ID.
    Она принимает: 1) db (Session) - активная сессия SQLAlchemy для работы с БД
    2) post_id (int) - ID поста, который нужно обновить.
    3) post_data (PostCreate) - Pydantic-схема, которая валидирует новые данные для поста.

    Функция возвращает ORM-объект обновленного поста, либо None, если пост не был найден.
    """
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None

    post.title = post_data.title
    post.content = post_data.content
    post.datetime = post_data.datetime
    post.user_id = post_data.user_id

    tags = db.query(Tag).filter(Tag.id.in_(post_data.tags)).all()
    post.tags = tags

    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post_id: int):
    """
    Эта функция удаляет пост из базы данных по его ID.
    Она принимает:
    1) db (Session) - активная сессия SQLAlchemy для работы с БД
    2) post_id (int) - ID поста, который нужно удалить.

    Функция возвращает True, если удаление прошло успешно, либо False, если пост не был найден.
    """
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return False

    db.delete(post)
    db.commit()
    return True


