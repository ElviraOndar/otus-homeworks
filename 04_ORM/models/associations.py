from sqlalchemy import Table, Column, Integer, ForeignKey
from db.session import base  # импортируй свой declarative_base()

post_tags = Table(
    'post_tags',
    base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)