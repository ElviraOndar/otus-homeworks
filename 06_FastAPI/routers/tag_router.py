from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.tag import Tag
from schemas.tag_schema import TagCreate, TagRead

router = APIRouter(prefix="/tags", tags=["Tags"])

@router.post("/", response_model=TagRead)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    """
    Создаёт новый тег в базе данных.

    Принимает:
    - tag: TagCreate — Pydantic-схему с названием тега
    - db: Session — подключение к базе

    Возвращает:
    - TagRead — созданный тег с его ID
    """
    new_tag = Tag(**tag.dict())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag