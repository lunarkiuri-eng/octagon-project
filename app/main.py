from fastapi import FastAPI
from app.api import categories, books

app = FastAPI(
    title="Book API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Сервис работает"}


@app.get("/")
def root():
    return {
        "message": "Добро пожаловать в Book API!",
        "docs": "/docs",
        "health": "/health"
    }