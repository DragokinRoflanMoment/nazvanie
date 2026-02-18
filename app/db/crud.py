from sqlalchemy.orm import Session
from .models import Book,Category
from app.schemas import CategoryCreate, BookCreate, BookUpdate

#для категорий

def create_category(db: Session, category: CategoryCreate):
    category = Category(title=category.title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_all_categories(db: Session):
    return db.query(Category).all()

def update_category(db: Session, category_id: int, title: str):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        category.title = title
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category

#книги

def create_book(db: Session, book: BookCreate):
    book = Book(
        title = book.title,
        description = book.description,
        price = book.price,
        url = book.url,
        category_id = book.category_id
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books_by_category_id(db: Session, category_id: int):
    return db.query(Book).filter(Book.category_id == category_id).all()

def get_all_books(db: Session):
    return db.query(Book).all()

def update_book(db: Session, book_id: int, book_data: BookUpdate):
    book = db.query(Book).filter(Book.id == book_id).first()
    
    if not book:
        return None
    
    book.title = book_data.title
    book.description = book_data.description
    book.price = book_data.price
    book.category_id = book_data.category_id
    book.url = book_data.url

    db.commit
    db.refresh(book)

    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book