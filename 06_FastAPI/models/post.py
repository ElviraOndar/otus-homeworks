from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from db.session import Base
from sqlalchemy.orm import relationship
from models.associations import post_tags


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    content = Column(Text, nullable=False)
    datetime = Column(DateTime, nullable=False)

    # Связь с пользователем, написавшим пост
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')

    # Связь поста с тегами
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')

