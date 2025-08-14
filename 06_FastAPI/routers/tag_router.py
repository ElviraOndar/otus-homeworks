from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crud.tag_crud import create_tag, get_tag, get_tags, update_tag, delete_tag
from schemas.tag_schema import TagCreate, TagRead

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/", response_model=TagRead)
def create_tag_endpoint(tag: TagCreate, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает POST-запрос: создать новый тег.
    Она принимает данные для нового тега в Pydantic-схеме TagCreate, которая содержит название тега.
    Затем функция вызывает из CRUD функцию create_tag.
    """
    return create_tag(db=db, tag=tag)


@router.get("/{tag_id}", response_model=TagRead)
def get_tag_endpoint(tag_id: int, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает GET-запрос: получить один тег по ID.
    """
    tag = get_tag(db=db, tag_id=tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return tag


@router.get("/", response_model=list[TagRead])
def get_tags_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает GET-запрос: получить список тегов.
    """
    return get_tags(db=db, skip=skip, limit=limit)


@router.put("/{tag_id}", response_model=TagRead)
def update_tag_endpoint(tag_id: int, new_tag: TagCreate, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает PUT-запрос: обновить тег по ID.
    """
    tag = update_tag(db=db, tag_id=tag_id, new_tag=new_tag)
    if not tag:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return tag


@router.delete("/{tag_id}")
def delete_tag_endpoint(tag_id: int, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает DELETE-запрос: удалить тег по ID.
    """
    success = delete_tag(db=db, tag_id=tag_id)
    if not success:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return {"message": "Тег успешно удалён"}
