from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=List[BookResponse])
def get_books(
    category_id: Optional[int] = Query(None, description="Фильтр по категории"),
    db: Session = Depends(get_db)
):
    if category_id:
        category = crud.get_category(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Категория не найдена")
        return crud.get_books_by_category(db, category_id)
    return crud.get_books(db)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book


@router.post("/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return crud.create_book(
        db=db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_title=category.title,
        url=book.url
    )


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    if book.category_id is not None:
        category = crud.get_category(db, book.category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Категория не найдена")

    if book.title is not None:
        db_book.title = book.title
    if book.description is not None:
        db_book.description = book.description
    if book.price is not None:
        db_book.price = book.price
    if book.url is not None:
        db_book.url = book.url
    if book.category_id is not None:
        db_book.category_id = book.category_id

    db.commit()
    db.refresh(db_book)
    return db_book


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    crud.delete_book(db, book_id)
    return None