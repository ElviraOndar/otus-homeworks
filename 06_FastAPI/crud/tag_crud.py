from sqlalchemy.orm import Session
from models.tag import Tag
from schemas.tag_schema import TagCreate


def create_tag(db: Session, tag_in: TagCreate):
    new_tag = Tag(name=tag_in.name)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()


