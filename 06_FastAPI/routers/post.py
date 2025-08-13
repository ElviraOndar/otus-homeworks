from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.post_schema import PostCreate, PostRead
from db.session import get_db
from services.post_service import create_post

router = APIRouter()

@router.post("/posts/", response_model=PostRead)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    db_post = create_post(db, post)
    return db_post  # FastAPI сам преобразует ORM -> PostRead