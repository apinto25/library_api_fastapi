from fastapi import FastAPI

app = FastAPI()

# Import and include your routers here
# from routers import example_router
# app.include_router(example_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI library API!"}
