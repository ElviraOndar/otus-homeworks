from fastapi import FastAPI
from db.session import engine, Base
from routers import post_router, user_router, tag_router


app = FastAPI(
    title="Real Madrid Blog API",
    description="API для блога про \"Реал Мадрид\"",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(post_router.router)
app.include_router(tag_router.router)
app.include_router(user_router.router)



# Пример корневого эндпоинта
@app.get("/")
def root():
    return {"message": "Добро пожаловать в API"}






