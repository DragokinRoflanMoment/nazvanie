from app.db.db import SessionLocal, engine, Base
from app.db.models import Category, Book
from app.db.crud import create_category,create_book,get_all_categories,get_all_books

Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    cat_fiction = create_category(db, title="Fiction")
    cat_western = create_category(db, title="Western")

    create_book(db,title="Amogus",description="Who Is Amogus",price=150.0,category_id=cat_fiction.id,url="")
    create_book(db,title="To Mars in 2025",description="Ilon Musk gg!",price=67.0,category_id=cat_fiction.id,url="")

    create_book(db,title="Red Dead Demention",description="Forgot about it, sry",price=222.0,category_id=cat_western.id,url="")
    create_book(db,title="Billy The CowBoy",description="How it feels to ride a horse instead of Harley Davidson", price=123.0,category_id=cat_western.id,url="")
finally:
    db.close()