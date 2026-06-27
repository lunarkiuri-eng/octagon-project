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