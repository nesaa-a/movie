from fastapi import FastAPI
from database import Base, engine
from routers import movies
from routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(movies.router, tags=["Movies"])
app.include_router(auth.router, tags=["Authentication"], prefix="/auth")