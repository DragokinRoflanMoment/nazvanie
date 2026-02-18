from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/", response_model=list[schemas.BookResponse])
def get_books(
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    if category_id:
        return crud.get_books_by_category_id(db,category_id)
    
    return crud.get_all_books(db)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db,book_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book

@router.post(
    "/",
    response_model=schemas.BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
):
    category = crud.get_category(db,book.category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category does not exist"
        )
    return crud.create_book(db,book)

@router.put("/{book_id}",response_model=schemas.BookResponse)
def update_book(
    book_id: int,
    book_data: schemas.BookUpdate,
    db: Session = Depends(get_db)
):
    if book_data.category_id is not None:
        category = crud.get_category(db,book_data.category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category does not exist"
            )
    
    updated = crud.update_book(db,book_id,book_data)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return updated

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db,book_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return

