from pydantic import BaseModel


# Базовая схема для тега
class TagBase(BaseModel):
    """Эта базовая Pydantic-схема содержит название тега.
        Используется как основа для других схем (создание, чтение)"""
    name: str


# Схема для создания нового тега
class TagCreate(TagBase):
    """Эта Pydantic-схема валидирует данные, которые вводятся для создания нового тега.
        Наследуется от TagBase без добавления новых полей"""
    pass


# Схема для чтения тега по запросу
class TagRead(TagBase):
    """Эта Pydantic-схема валидирует данные, которые будут отправлены клиенту о запрошенном теге.
        Наследуется от TagBase и добавляет поле id - ID тега"""
    id: int

    class Config:
        from_attributes = True

