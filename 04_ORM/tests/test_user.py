from models.user import User
from models.post import Post
from models.tag import Tag
from datetime import datetime


def test_create_user(session):
    """Эта функция проверяет создание и сохранение пользователя в базе данных"""
    user = User(name='Pep Guardiola')
    session.add(user)
    session.commit()

    # Извлекаем пользователя из базы и проверяем его имя
    retrieved_user = session.query(User).filter_by(name='Pep Guardiola').one_or_none()
    assert retrieved_user.name == 'Pep Guardiola'
    assert isinstance(retrieved_user.id, int)


def test_user_posts_relationship(session):
    """Эта функция проверяет связь 'один ко многим' между User и Post"""
    user = User(name='Zinedine Zidane')
    post1 = Post(title='Title 1', content='Content 1', DateTime=datetime.now(), user_id=user.id)
    post2 = Post(title='Title 2', content='Content 2', DateTime=datetime.now(), user_id=user.id)

    # Устанавливаем связь - добавляем посты пользователю
    user.posts.extend([post1, post2])

    session.add_all([user, post1, post2])
    session.commit()

    retrieved_user = session.query(User).filter_by(name='Zinedine Zidane').one()
    assert len(retrieved_user.posts) == 2
    assert retrieved_user.posts[0].title == 'Title 1'
    assert retrieved_user.posts[1].title == 'Title 2'


