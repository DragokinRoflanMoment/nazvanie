from sqlalchemy.orm import Session
from .models import Book,Category

#для категорий

def create_category(db: Session, title: str):
    category = Category(title=title)
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

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = None):
    book = Book(
        title = title,
        description = description,
        price = price,
        url = url,
        category_id = category_id
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_all_books(db: Session):
    return db.query(Book).all()

def update_book(db: Session, book_id: int, title: str = None, description: str = None, price: float = None, category_id: int = None, url: str = None):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        if title is not None:
            book.title = title
        if description is not None:
            book.description = description
        if price is not None:
            book.price = price
        if category_id is not None:
            book.category_id = category_id
        if url is not None:
            book.url = url
        db.commit()
        db.refresh(book)
    return

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book