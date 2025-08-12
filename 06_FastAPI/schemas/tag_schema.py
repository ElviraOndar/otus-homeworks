from pydantic import BaseModel


# Базовая схема (общие поля)
class TagBase(BaseModel):
    name: str


# Схема для создания нового тега
class TagCreate(TagBase):
    pass


# Схема для чтения (возврат клиенту)
class TagRead(TagBase):
    id: int

    class Config:
        from_attributes = True

