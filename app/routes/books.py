from typing import List, Optional  # noqa

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import Book, get_db_session
from app.schema import BookCreate, BookRead, BookUpdate

book_router = APIRouter(prefix="/books", tags=["Books"])


@book_router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreate, db_session: Session = Depends(get_db_session)
) -> Book:
    new_book = Book(**book.model_dump())
    db_session.add(new_book)
    db_session.commit()
    db_session.refresh(new_book)
    return new_book


@book_router.get("/", response_model=List[BookRead])
def get_all_books(db_session: Session = Depends(get_db_session)) -> List[Book]:
    books = db_session.exec(select(Book)).all()
    return books


@book_router.get("/{book_id}", response_model=BookRead)
def get_book_by_id(book_id: int, db_session: Session = Depends(get_db_session)) -> Book:
    book = db_session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.patch("/{book_id}", response_model=BookRead)
def update_book(
    book_id: int, book_update: BookUpdate, db_session: Session = Depends(get_db_session)
) -> Book:
    book = db_session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    updated_book_data = book_update.model_dump(exclude_unset=True)
    book.sqlmodel_update(updated_book_data)

    db_session.add(book)
    db_session.commit()
    db_session.refresh(book)
    return book


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db_session: Session = Depends(get_db_session)):
    book = db_session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_session.delete(book)
    db_session.commit()
    return {"message": "Book deleted successfully"}
