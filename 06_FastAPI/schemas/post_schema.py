from datetime import datetime
from typing import List
from pydantic import BaseModel
from user_schema import UserRead
from tag_schema import TagRead


# ===== Базовая схема =====
class PostBase(BaseModel):
    title: str
    content: str
    datetime: datetime


# ===== Схема для создания =====
class PostCreate(PostBase):
    user_id: int
    tags: List[int]  # список id тегов


# ===== Схема для чтения =====
class PostRead(PostBase):
    id: int
    user: UserRead
    tags: List[TagRead]

    class Config:
        from_attributes = True


