from pydantic import BaseModel
from typing import Union
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class MovieCreate(BaseModel):
    title: str
    category: str
    release_year: int
    description: Union[str, None] = None  # Përdor Union për tipet opsionale
    user_id: int

class MovieUpdate(BaseModel):
    title: Union[str, None] = None
    category: Union[str, None] = None
    release_year: Union[int, None] = None
    description: Union[str, None] = None
