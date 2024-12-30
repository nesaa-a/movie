from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Movie, User
from schemas import MovieCreate, MovieUpdate
import pandas as pd

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == movie.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.get("/")
def read_movies(user_id: int, db: Session = Depends(get_db)):
    return db.query(Movie).filter(Movie.user_id == user_id).all()


@router.put("/{movie_id}")
def update_movive(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie Not Found!")

    update_data = movie.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_movie, key, value)
    
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(db_movie)
    db.commit()
    return {"message": "Movie deleted successfully"}

@router.get("/report")
def movie_report(user_id: int, db: Session = Depends(get_db)):
    movies = db.query(Movie).filter(Movie.user_id == user_id).all()
    movies_df = pd.DataFrame([{"title": m.title, "category": m.category, "release_year": m.release_year} for m in movies])

    if movies_df.empty:
        return {"message": "No movies found"}

    report = movies_df.groupby("category")["title"].count().to_dict()
    return {"report": report}
