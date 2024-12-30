from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Krijo një SQLite Database
DATABASE_URL = "sqlite:///./movies.db"

# Inicializimi i motorit të bazës së të dhënave
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Krijo sesionin e bazës së të dhënave
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Krijo një bazë për modelet
Base = declarative_base()


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()