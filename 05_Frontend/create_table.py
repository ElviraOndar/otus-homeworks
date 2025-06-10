from db.session import engine, base
from models.post import Post
from models.user import User
from models.tag import Tag


if __name__ == '__main__':
    base.metadata.create_all(engine)



