from models.user import User
from models.post import Post
from models.tag import Tag
from datetime import datetime


def test_create_tag(session):
    """Эта функция тестирует создание и сохранение тега в базе данных"""
    tag = Tag(name='Test Tag')
    session.add(tag)
    session.commit()

    retrieved_tag = session.query(Tag).filter_by(name='Test Tag').one_or_none()
    assert retrieved_tag is not None
    assert retrieved_tag.name == 'Test Tag'


def test_tag_post_relationship(session):
    """Эта функция 1) создает пользователя,
    2) создает пост, 3) создает два тега,
    4) проверяет, что установилась связь между постом и тегами"""
    user = User(name="Rafa Benitez")
    session.add(user)
    session.commit()

    post = Post(title="Test Post", content="Content", DateTime=datetime.now(), user_id=user.id)

    tag1 = Tag(name="La Liga")
    tag2 = Tag(name="Champions League")

    post.tags.extend([tag1, tag2])

    session.add(post)
    session.commit()

    assert len(post.tags) == 2
    assert tag1 in post.tags
    assert tag2 in post.tags
    assert post in tag1.posts
    assert post in tag2.posts



