from db.session import SessionLocal
from models.post import Post
from models.user import User
from models.tag import Tag
from datetime import datetime


session = SessionLocal()

# Создаем двух пользователей
user1 = User(name='Carlo Ancelotti')
user2 = User(name='Jose Mourinho')

# Создаем три тега
tag_interview = Tag(name='interview')
tag_appointment = Tag(name='appointment')
tag_reward = Tag(name='reward')
tag_news = Tag(name='news')
tag_anniversary = Tag(name='anniversary')

# Создаём пять постов от двух пользователей с использованием тегов
post1 = Post(
    title="First Xabi Alonso's interview as a head coach of Real Madrid",
    content="I will try to make sure that together we build a team that we are proud of and that generates excitement",
    DateTime=datetime.now(),
)
post1.user = user1
post1.tags = [tag_interview, tag_appointment]

post2 = Post(
    title="Alvaro Arbeloa becomes a head coach of Real Madrid Castilla",
    content="Alvaro Arbeloa will be Castilla's manager starting in the 2025-2026 season",
    DateTime=datetime.now(),
)
post2.user = user2
post2.tags = [tag_news, tag_appointment]

post3 = Post(
    title="Mbappe named Real Madrid's Player of the Season",
    content="""Kylian Mbappé received the Best Player Award 
    from Real Madrid for the 2024/25 season. The forward was honored 
    after a spectacular first season at the club, with 43 goals in 56 matches.""",
    DateTime=datetime.now(),
)
post3.user = user1
post3.tags = [tag_news, tag_reward]

post4 = Post(
    title="Third anniversary of the 14th Champions League title",
    content="""On May 28, 2022, Real Madrid defeated Liverpool 0-1 in Paris and won 
    a historic Champions League title with unforgettable comebacks at the Bernabéu.""",
    DateTime=datetime.now(),
)
post4.user = user1
post4.tags = [tag_anniversary]

post5 = Post(
    title="Carvajal received the Gold Medal of the Community of Madrid",
    content="""Daniel Carvajal was awarded the Gold Medal of the Community 
    of Madrid at an event attended by President Florentino Pérez.""",
    DateTime=datetime.now(),
)
post5.user = user2
post5.tags = [tag_news, tag_reward]

session.add_all([post1, post2, post3, post4, post5, user1, user2, tag_interview,
                 tag_appointment, tag_reward, tag_news, tag_anniversary])

session.commit()

session.close()







