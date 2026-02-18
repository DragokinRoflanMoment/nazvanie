from app.db.db import SessionLocal, engine
from app.api import categories
from app.api import books
from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection success")
    except Exception as e:
        print("Database connection failed:", e)
    
    yield

    print("Closing app")

app = FastAPI()
app.include_router(categories.router)
app.include_router(books.router)

db = SessionLocal()

@app.get("/health")
def health_check():
    return {"status": "ok"}


db.close()