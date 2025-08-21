# FastAPI Real Madrid Blog

Блог о мадридском "Реале" на **FastAPI** с подключением к базе данных **PostgreSQL** внутри Docker-контейнера.  

Проект демонстрирует работу с моделями пользователей, постов и тегов, а также предоставляет удобный веб-интерфейс для API-документации.

---

## 📌 Описание
Цель проекта — показать основы работы с FastAPI, PostgreSQL и Docker Compose.  
Функциональность:
- работа с пользователями, постами и тегами;
- API-документация доступна через `/docs/`;
- в `/posts/` и `/posts/{post_id}` доступна HTML-страница;
- в `/posts/info/all` и `/posts/{post_id}` можно получить JSON со всеми постами, либо с конкретным постом;
- все остальные эндпоинты также возвращают JSON.

---

## ⚙️ Установка

1. **Клонируем репозиторий и переходим в папку проекта:**

```bash
git clone https://github.com/ElviraOndar/otus-homeworks.git
cd otus-homeworks/06_FastAPI
```

**Собираем и запускаем контейнеры:**

```bash

docker-compose up -d --build
```
## 🚀 Использование

После запуска контейнеров проект будет доступен по адресу:

```bash
http://localhost:8001
```

Документация API: http://localhost:8001/docs

HTML-страница с постами: http://localhost:8001/posts

JSON со списком постов: http://localhost:8001/posts/info/all

## 🗄️ Работа с БД

**1. Создание таблиц**

Чтобы создать таблицы внутри базы данных, используйте эту команду:

```bash
docker exec -it real_fastapi python create_tables.py
```

**2. Заполнение базы начальными данными**

Чтобы заполнить таблицы тестовыми данными, используйте эту команду:

```bash
docker exec -it real_fastapi python seed_data.py
```

## 📂 Структура проекта

```bash
06_FastAPI/
│── db/  
│   └── session.py        # Подключение к БД  
│── models/  
│   ├── post.py           # Модель Post  
│   ├── user.py           # Модель User  
│   └── tag.py            # Модель Tag  
│── static/  
│   └── style.css         # Стили проекта  
│── templates/  
│   ├── index.html        # Главная страница со списком постов  
│   ├── post_detail.html  # Страница отдельного поста  
│   └── contacts.html     # Страница с контактами  
│── seed_data.py          # Скрипт для заполнения базы начальными данными  
│── create_tables.py      # Скрипт для создания таблиц  
│── main.py               # Точка входа FastAPI-приложения  
│── Dockerfile            # Описание сборки контейнера  
│── docker-compose.yml    # Настройка сервисов (real_web + real_db)  
│── requirements.txt      # Зависимости проекта  
│── .env                  # Конфигурация окружения (DATABASE_URL) 

```

## ✅ Примечания

Сервер Uvicorn запускать вручную не нужно, так как команда уже прописана в Dockerfile.

Все таблицы и данные создаются внутри контейнера PostgreSQL.

Проверить таблицы можно, подключившись к базе:

```bash
docker exec -it real_postgres psql -U user -d realdb
```
