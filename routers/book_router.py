from fastapi import APIRouter, HTTPException
from models.books import Book
from typing import List

book_router = APIRouter()

books: List[Book] = []


@book_router.get("/books", response_model=List[Book])
def get_books():
    return books


@book_router.post("/books", response_model=Book)
def create_book(book: Book):
    books.append(book)
    return book


@book_router.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
