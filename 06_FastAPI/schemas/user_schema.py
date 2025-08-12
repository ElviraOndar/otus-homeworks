from pydantic import BaseModel


# Базовая схема
class UserBase(BaseModel):
    name: str


# Для создания нового пользователя
class UserCreate(UserBase):
    pass


# Для чтения (возврат клиенту)
class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True



