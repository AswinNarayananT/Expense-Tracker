from fastapi import FastAPI
from .routes import auth

app =FastAPI()

app.include_router(auth.router)


@app.get("/")
def home():
    return {"api":"running successfully"}