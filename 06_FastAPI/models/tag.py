from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base
from models.associations import post_tags


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    posts = relationship('Post', secondary=post_tags, back_populates='tags')

