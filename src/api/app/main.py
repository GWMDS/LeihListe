from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan function, used to do stuff before or after server is online"""
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])
