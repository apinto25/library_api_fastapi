from fastapi import FastAPI
from routers.book_router import book_router

app = FastAPI()

app.include_router(book_router)


@app.get("/")
def read_root():
    """
    Return a welcome message for the FastAPI library API root endpoint.
    
    Returns:
        dict: A JSON-compatible dictionary containing the welcome message.
    """
    return {"message": "Welcome to the FastAPI library API!"}
