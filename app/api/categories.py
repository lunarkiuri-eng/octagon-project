from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.db import get_db
from app.db import crud
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category


@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_title(db, category.title)
    if db_category:
        raise HTTPException(status_code=400, detail="Категория с таким названием уже существует")
    return crud.create_category(db, category.title)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    if category.title is not None:
        existing = crud.get_category_by_title(db, category.title)
        if existing and existing.id != category_id:
            raise HTTPException(status_code=400, detail="Категория с таким названием уже существует")
        db_category.title = category.title
        db.commit()
        db.refresh(db_category)
    
    return db_category


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    crud.delete_category(db, category_id)
    return None