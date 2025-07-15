from fastapi import APIRouter, HTTPException
from models.books import Book
from typing import List

book_router = APIRouter()

books: List[Book] = []


@book_router.get("/books", response_model=List[Book])
def get_books():
    """
    Retrieve the full list of books.
    
    Returns:
        List[Book]: A list containing all books currently stored in memory.
    """
    return books


@book_router.post("/books", response_model=Book)
def create_book(book: Book):
    """
    Add a new book to the collection and return the created book.
    
    Parameters:
        book (Book): The book object to add.
    
    Returns:
        Book: The newly added book.
    """
    books.append(book)
    return book


@book_router.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int):
    """
    Retrieve a book from the collection by its ID.
    
    Parameters:
        book_id (int): The unique identifier of the book to retrieve.
    
    Returns:
        Book: The book object with the specified ID.
    
    Raises:
        HTTPException: If no book with the given ID is found, raises a 404 error.
    """
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
