from typing import Optional, List
from db.session import Session
from models.tag import Tag
from models.user import User
from models.post import Post


def get_user_posts(name: Optional[str] = None, user_id: Optional[int] = None) -> List[Post]:
    """
    Эта функция возвращает список постов пользователя по его имени или id.
    Если пользователь не найден, то возвращает пустой список.
    """
    with Session() as session:
        query = session.query(User)

        if user_id is not None:
            query = query.filter(User.id == user_id)
        elif name is not None:
            query = query.filter(User.name == name)
        else:
            # Если ни имя, ни id не указаны, возвращаем пустой список
            return []

        user = query.one_or_none()

        if user:
            return user.posts
        else:
            return []


if __name__ == '__main__':
    # Получаем все посты от пользователя Carlo Ancelotti по его имени
    posts = get_user_posts(name='Carlo Ancelotti')
    print('Carlo Ancelotti posts:', len(posts))
    for post in posts:
        print(f"Title: '{post.title}', "
              f"date and time: {post.DateTime.strftime("%Y-%m-%d, %H:%M:%S")}")

    # Получаем все посты от пользователя Jose Mourinho по его user_id
    posts_2 = get_user_posts(user_id=2)
    print('Jose Mourinho posts:', len(posts_2))
    for post in posts_2:
        print(f"Title: '{post.title}', "
              f"date and time: {post.DateTime.strftime("%Y-%m-%d, %H:%M:%S")}")

