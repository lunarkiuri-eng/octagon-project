from pydantic import BaseModel
from typing import Optional

# Схемы для категорий

# Базовая схема категории
class CategoryBase(BaseModel):
    title: str

# Схема для создания категории 
class CategoryCreate(CategoryBase):
    pass

# Схема для обновления категории 
class CategoryUpdate(BaseModel):
    title: Optional[str] = None

# Схема ответа 
class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True  # Включает orm_mode для работы с SQLAlchemy


#Схемы для книг

# Базовая схема книги 
class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: Optional[str] = ""
    category_id: int

# Схема для создания книги 
class BookCreate(BookBase):
    pass

# Схема для обновления книги 
class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

# Схема ответа для книги 
class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True  # Включает orm_mode для работы с SQLAlchemy