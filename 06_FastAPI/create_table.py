from db.session import engine, Base
from models.post import Post
from models.user import User
from models.tag import Tag


if __name__ == '__main__':
    Base.metadata.create_all(engine)



