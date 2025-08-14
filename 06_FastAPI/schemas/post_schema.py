from datetime import datetime
from typing import List
from pydantic import BaseModel
from .user_schema import UserRead  # объект автора поста, содержащий ID и имя автора
from .tag_schema import TagRead  # объект тегов поста, содержащий ID и названия тегов


# ===== Базовая схема поста =====
class PostBase(BaseModel):
    """
    Это базовая Pydantic-схема для модели поста.
    Она содержит поля, общие для всех операций с постами, -- создание, чтение, обновление и удаление.
    Используется как родительский класс для более специализированных схем -- PostCreate и PostRead
    """
    title: str
    content: str
    datetime: datetime


# ===== Схема для создания поста =====
class PostCreate(PostBase):
    """
    Это Pydantic-схема валидирует данные, которые принимаются для создания нового поста.
    Она наследуется от PostBase и добавляет поля:
        - user_id: ID пользователя - автора поста;
        - tags: список ID тегов, которые будут привязаны к посту.
    """
    user_id: int
    tags: List[int]


# ===== Схема для чтения поста =====
class PostRead(PostBase):
    """
    Это Pydantic-схема валидирует данные, которые будут возвращаться клиенту.
    Наследуется от PostBase и добавляет поля:
    - id: ID запрошенного поста.
    - user: объект автора поста (его имя и id).
    - tags: список тегов, связанных с постом.
    """
    id: int
    user: UserRead
    tags: List[TagRead]

    class Config:
        from_attributes = True


