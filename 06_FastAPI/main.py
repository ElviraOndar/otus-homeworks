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


@app.get("/posts/{post_id}", response_class=HTMLResponse)
def post_detail(post_id: int, request: Request, db: Session = Depends(get_db)):
    post = get_post(db, post_id)
    if not post:
        return RedirectResponse("/")
    return templates.TemplateResponse("post_detail.html", {"request": request, "post": post})


# Форма создания поста
@app.get("/create", response_class=HTMLResponse)
def create_post_form(request: Request):
    return templates.TemplateResponse("create_post.html", {"request": request})


# Обработка создания поста
@app.post("/posts/")
def create_post_handler(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    tags_list = [int(t.strip()) for t in tags.split(",") if t.strip()]
    new_post = PostCreate(
        title=title,
        content=content,
        datetime=datetime.now(),
        user_id=user_id,
        tags=tags_list
    )
    post = create_post(db, new_post)
    return RedirectResponse(f"/posts/{post.id}", status_code=303)


# запуск
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)




