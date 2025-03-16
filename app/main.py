from fastapi import FastAPI
from app.presentation.routers import hello

app = FastAPI()

app.include_router(hello.router)