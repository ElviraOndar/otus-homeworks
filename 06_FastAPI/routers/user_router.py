from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.user_schema import UserCreate, UserRead
from crud.user_crud import create_user, get_user, get_users, update_user, delete_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает POST-запрос: создать нового пользователя.
    Она принимает Pydantic-схему UserCreate, которая содержит данные для нового пользователя, -- его имя.
    Вызывает из CRUD функцию create_user.
    Возвращает новый ORM-объект User, но при помощи response_model преобразует данные
    в Pydantic-схему UserRead, которая содержит имя пользователя и его ID.
    """
    return create_user(db=db, user=user)


@router.get("/{user_id}", response_model=UserRead)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает GET-запрос: получить одного пользователя по ID.
    Она вызывает из CRUD функцию get_user.
    """
    user = get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@router.get("/", response_model=list[UserRead])
def get_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает GET-запрос: получить список пользователей.
    Она вызывает из CRUD функцию get_users.
    """
    return get_users(db=db, skip=skip, limit=limit)


@router.put("/{user_id}", response_model=UserRead)
def update_user_endpoint(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает PUT-запрос: обновить данные пользователя по ID.
    Она вызывает из CRUD функцию update_user.
    """
    user = update_user(db=db, user_id=user_id, user_data=user_data)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Эта функция обрабатывает DELETE-запрос: удалить пользователя по ID.
    Она вызывает из CRUD функция delete_user.
    """
    success = delete_user(db=db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"message": "Пользователь успешно удален"}

