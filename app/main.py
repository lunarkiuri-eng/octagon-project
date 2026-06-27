from app.db.db import SessionLocal
from app.db.crud import get_books, get_categories
def print_data():
    db = SessionLocal()
    try:
        print("\nСписок книг:")
        books = get_books(db)
        if books:
            for book in books:
                category_title = book.category.title if book.category else "Без категории"
                print(f" {book.title} — {category_title} ({book.price} руб.)")
        else:
            print("  Книг пока нет.")

        print("\nКатегории:")
        categories = get_categories(db)
        if categories:
            for category in categories:
                print(f" {category.title} — {len(category.books)} книг")
        else:
            print("  Категорий пока нет.")
    finally:
        db.close()

if __name__ == "__main__":
    print_data()