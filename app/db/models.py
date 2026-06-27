from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

# Таблица "categories"
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String, nullable=False, unique=True) 

    # Связь с книгами (одна категория — много книг)
    books = relationship("Book", back_populates="category")

# Таблица "books" 
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)   
    title = Column(String, nullable=False)               
    description = Column(String)                         
    price = Column(Float)                               
    url = Column(String, default="")                     
    
    # Внешний ключ — ссылка на таблицу categories
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Связь с категорией
    category = relationship("Category", back_populates="books")