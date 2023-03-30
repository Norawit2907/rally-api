from fastapi import FastAPI
from app.routers import users, reviews

app = FastAPI()

app.include_router(users.router)
app.include_router(reviews.router)

@app.get("/")
def read_root():
    return {"Hello": "world"}