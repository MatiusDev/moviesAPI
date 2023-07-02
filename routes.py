from fastapi import APIRouter, Depends

from api.movie import router as movie_router
from api.user import router as user_router

from middlewares.jwt_auth import JWTBearer

routes = APIRouter()

routes.include_router(movie_router, prefix="/movies", dependencies=[Depends(JWTBearer())])
routes.include_router(user_router, prefix="/users")
