from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from schemas.user_schema import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Создать нового пользователя.

    - **name**: имя пользователя
    """
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    """
    Получить список всех пользователей.
    """
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Получить пользователя по ID.

    - **user_id**: идентификатор пользователя
    """
    return db.query(User).filter(User.id == user_id).first()