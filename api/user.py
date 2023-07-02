from fastapi import APIRouter

from models.schemas.user import UserCreate as User

from utils.jwt_manager import create_token

router = APIRouter()

@router.post('/login', tags=['auth'], response_model=str, status_code=200)
def login(user: User) -> str:
  if user.email and user.password:
    token = create_token(user.dict())
  return token