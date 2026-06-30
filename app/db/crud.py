from sqlalchemy.orm import Session
from app.db import models

def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category_by_title(db: Session, title: str):
    return db.query(models.Category).filter(models.Category.title == title).first()

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session):
    return db.query(models.Category).all()

def create_book(db: Session, title: str, description: str, price: float, category_title: str, url: str = ""):
    category = get_category_by_title(db, category_title)
    if not category:
        category = create_category(db, category_title)
    
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category.id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books_by_category(db: Session, category_id: int):
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

#для обновления категорий
def update_category(db: Session, category_id: int, title: str):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db_category.title = title
        db.commit()
        db.refresh(db_category)
    return db_category


#для обновления книг
def update_book(db: Session, book_id: int, title: str = None, description: str = None, price: float = None, category_id: int = None):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        if title is not None:
            db_book.title = title
        if description is not None:
            db_book.description = description
        if price is not None:
            db_book.price = price
        if category_id is not None:
            category = db.query(models.Category).filter(models.Category.id == category_id).first()
            if category:
                db_book.category_id = category_id
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category