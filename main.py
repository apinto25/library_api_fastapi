from fastapi import FastAPI
from routers.book_router import book_router

app = FastAPI()

app.include_router(book_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI library API!"}
