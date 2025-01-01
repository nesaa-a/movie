import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import movies
from backend.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(movies.router, tags=["Movies"])
app.include_router(auth.router, tags=["Authentication"], prefix="/auth")