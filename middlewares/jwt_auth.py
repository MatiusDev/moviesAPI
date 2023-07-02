from fastapi.requests import Request
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException

from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
  async def __call__(self, request: Request):
    auth = await super().__call__(request)
    payload = validate_token(auth.credentials)
    print(payload)
    if payload['email'] != "admin@example.com":
      raise HTTPException(status_code=403, detail="Credenciales invalidas")