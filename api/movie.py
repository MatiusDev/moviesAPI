from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from config.database import SessionLocal, get_db

from models.schemas.movie import Movie, MovieBase
from services.movie import MovieService

router = APIRouter()

@router.get('/', tags=['movies'], response_model=List[Movie])
def get_movies(db: SessionLocal = Depends(get_db)) -> List[Movie]:
  return MovieService(db).get_movies()

@router.get('/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int, db: SessionLocal = Depends(get_db)) -> Movie:
  movie = MovieService(db).get_movie(id)
  if not movie:
    raise HTTPException(status_code=404, detail="No se ha encontrado la pelicula")
  return movie

@router.get('/category/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str, db: SessionLocal = Depends(get_db)) -> List[Movie]:
  movies = MovieService(db).get_movie_by_category(category)
  if not movies:
    raise HTTPException(status_code=404, detail="No se encontraron peliculas en esa categoria.")
  return movies

@router.post('/', tags=['movies'], response_model=Movie, status_code=201)
def create_movie(movie: MovieBase, db: SessionLocal = Depends(get_db)) -> Movie:
  return MovieService(db).create_movie(movie)

@router.put('/{id}', tags=['movies'], response_model=Movie, status_code=201)
def update_movie(id: int, movie: MovieBase, db: SessionLocal = Depends(get_db)) -> Movie:
  db_movie = MovieService(db).get_movie(id)
  if not db_movie:
    raise HTTPException(status_code=404, detail="No se ha encontrado la pelicula")
  return MovieService(db).update_movie(id, movie)

@router.delete('/{id}', tags=['movies'], response_model=str)
def delete_movie(id: int, db: SessionLocal = Depends(get_db)) -> str:
  MovieService(db).delete_movie(id)
  return "El registro se ha eliminado correctamente."