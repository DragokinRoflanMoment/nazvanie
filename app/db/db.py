from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#данные БД
DB_URL = "postgresql://octagon:1@localhost:5432/octagon_db"

engine = create_engine(DB_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()