from typing import List

from config.database import SessionLocal

from models.schemas.movie import Movie, MovieBase
from models.db_models.movie import MovieModel

class MovieService():  
  def __init__(self, db: SessionLocal) -> None:
    self.db = db
    
  def get_movies(self) -> List[Movie]:
    return self.db.query(MovieModel).all()
  
  def get_movie(self, id: int):
    return self.db.query(MovieModel).filter(MovieModel.id == id).first()
  
  def get_movie_by_category(self, category: str) -> List[Movie]:
    return self.db.query(MovieModel).filter(MovieModel.category == category).all()
  
  def create_movie(self, movie: MovieBase):
    new_movie = MovieModel(**movie.dict())
    self.db.add(new_movie)
    self.db.commit()
    self.db.refresh(new_movie)
    return new_movie 
  
  def update_movie(self, id: int, movie: MovieBase):
    updated_movie = self.db.query(MovieModel).filter(MovieModel.id == id).update(movie.dict(), synchronize_session=False)
    self.db.commit()
    self.db.refresh(updated_movie)
    return updated_movie
  
  def delete_movie(self, id: int) -> None:
    movie = self.get_movie(id)
    self.db.delete(movie)
    self.db.commit()
    