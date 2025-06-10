from models.user import User
from models.post import Post
from datetime import datetime
from queries import get_user_posts


def test_get_user_posts(session):
    """Эта функция 1) создает объект модели User,
    2) создает объект модели Post,
    3) вызывает функцию get_user_posts и проверяет,
    корректно ли она возвращает количество постов,
    название поста и содержание поста"""
    user = User(name="Jose Mourinho")
    session.add(user)
    session.commit()

    post = Post(title="Test Title", content="Test Content", DateTime=datetime.now(), user_id=user.id)
    session.add(post)
    session.commit()

    posts = get_user_posts(session, name="Jose Mourinho")
    assert len(posts) == 1
    assert posts[0].title == "Test Title"
    assert posts[0].content == "Test Content"


