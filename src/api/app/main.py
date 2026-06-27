from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session
from routers import items, customers, borrowings
from dependencies import write_starting_data
from database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan function, used to do stuff before or after server is online"""
    SQLModel.metadata.create_all(engine)
    write_starting_data(Session(engine))
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(
    items.router
)

app.include_router(
    customers.router
)

app.include_router(
    borrowings.router
)
