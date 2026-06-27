from app.db.db import SessionLocal
from app.db.crud import create_category, create_book
from app.db.models import Base
from app.db.db import engine

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    
    try:
        categories_data = {
            "Программирование": [
                {"title": "Python для начинающих", "description": "Основы Python", "price": 1200.0},
                {"title": "SQL для аналитиков", "description": "Работа с базами данных", "price": 1500.0},
                {"title": "Алгоритмы и структуры данных", "description": "Глубокое понимание алгоритмов", "price": 1800.0},
            ],
            "Художественная литература": [
                {"title": "Мастер и Маргарита", "description": "Роман Михаила Булгакова", "price": 800.0},
                {"title": "Преступление и наказание", "description": "Роман Фёдора Достоевского", "price": 700.0},
                {"title": "Война и мир", "description": "Роман Льва Толстого", "price": 900.0},
            ]
        }
        for category_title, books in categories_data.items():
            for book_data in books:
                create_book(
                    db=db,
                    title=book_data["title"],
                    description=book_data["description"],
                    price=book_data["price"],
                    category_title=category_title
                )
                print(f"Добавлена книга: {book_data['title']} в категорию '{category_title}'")
        
        print("База данных инициализирована!")
        
    finally:
        db.close()

if __name__ == "__main__":
    init_db()