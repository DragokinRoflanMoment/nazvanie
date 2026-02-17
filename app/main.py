from app.db.db import SessionLocal
from app.db.crud import get_all_categories,get_all_books

db = SessionLocal()

print("Категории:")
for cat in get_all_categories(db):
    print(f"{cat.id}: {cat.title}")

print("Книги:")
for book in get_all_books(db):
    print(f"{book.id}: {book.title} ({book.category.title}) | {book.price} RUB")

db.close()