from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserCreate
from models import user


def create_user(db: Session, user_in: UserCreate):
    new_user = User(name=user_in.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
