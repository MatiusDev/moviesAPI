from pydantic import BaseModel, Field
from typing import Optional

class MovieBase(BaseModel):
  title: str = Field(min_length=5, max_length=15)
  overview: str = Field(min_length=15, max_length=40)
  year: int = Field(le=2023)
  rating: float
  category: str
  
  class Config:
    schema_extra = {
      "example": {
        "title": "Movie",
        "overview": "Movie description",
        "year": 2023,
        "rating": 0,
        "category": "Unknow"
      }
    }

class Movie(MovieBase):
  id: Optional[int] = None
  
  class Config:
    schema_extra = {
      "example": {
        "id": 1,
        "title": "Movie",
        "overview": "Movie description",
        "year": 2023,
        "rating": 0,
        "category": "Unknow"
      }
    }
    orm_mode = True