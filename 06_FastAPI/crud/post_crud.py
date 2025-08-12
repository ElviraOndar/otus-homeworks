from sqlalchemy.orm import Session, joinedload
from models.post import Post
from models.tag import Tag
from schemas.post_schema import PostCreate


def create_post(db: Session, post: PostCreate):
    new_post = Post(
        title=post.title,
        content=post.content,
        DateTime=post.DateTime,
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
    return (
        db.query(Post)
        .options(
            joinedload(Post.user),
            joinedload(Post.tags)
        )
        .filter(Post.id == post_id)
        .first()
    )

# Создать delete post и udpate post, а также создать эти функции для tag и user