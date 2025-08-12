from sqlalchemy.orm import Session, joinedload
from models.post import Post
from models.tag import Tag
from schemas.post_schema import PostCreate


def create_post(db: Session, post_in: PostCreate):
    new_post = Post(
        title=post_in.title,
        content=post_in.content,
        datetime=post_in.datetime,
        user_id=post_in.user_id
    )

    # Привязываем теги по id
    if post_in.tags:
        tags = db.query(Tag).filter(Tag.id.in_(post_in.tags)).all()
        new_post.tags = tags

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_post(db: Session, post_id: int):
    return (
        db.query(Post)
        .options(joinedload(Post.user), joinedload(Post.tags))
        .filter(Post.id == post_id)
        .first()
    )