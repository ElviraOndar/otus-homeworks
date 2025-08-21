from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from db.session import get_db
from crud.post_crud import get_posts, get_post, create_post
from schemas.post_schema import PostCreate
from datetime import datetime
import uvicorn
from routers import post_router, user_router, tag_router


app = FastAPI(
    title="Real Madrid Blog API",
    description="API для блога про \"Реал Мадрид\"",
    version="1.0.0"
)

# Подключаем папку со статикой
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем шаблоны
templates = Jinja2Templates(directory="templates")

# Подключаем роутеры
app.include_router(post_router.router)
app.include_router(tag_router.router)
app.include_router(user_router.router)


# Корневой эндпоинт
@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    posts = get_posts(db)
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})


# Эндпоинт с контактами
@app.get("/contacts", response_class=HTMLResponse)
def get_contacts(request: Request):
    """
    Возвращает HTML-страницу с контактами
    """
    return templates.TemplateResponse("contacts.html", {"request": request})


# запуск
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)




