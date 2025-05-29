from models.user import User
from models.post import Post
from models.tag import Tag
from datetime import datetime


def test_create_post(session):
    """Эта функция 1) создает объект модели User,
    2) создает объект модели Post,
    3) проверяет корректность данных в посте, который сохранился в базе данных"""
    user = User(name='Xabi Alonso')
    session.add(user)
    session.commit()

    post = Post(title='Test Post Title', content='Test Post Content', DateTime=datetime.now(), user_id=user.id)
    user.posts.extend([post])
    session.add_all([user, post])
    session.commit()

    # Извлекаем пост из базы и проверяем его название и содержание
    retrieved_post = session.query(Post).first()
    assert retrieved_post.title == 'Test Post Title'
    assert retrieved_post.content == 'Test Post Content'
    assert retrieved_post.user_id == user.id
    assert retrieved_post.DateTime is not None


