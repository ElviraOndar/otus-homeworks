from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Связь - у пользователя может быть много постов
    posts = relationship('Post', back_populates='user')

