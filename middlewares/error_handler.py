from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
  def __init__(self, app: FastAPI) -> None:
    super().__init__(app)
  
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response | JSONResponse:
    try:
      return await call_next(request)
    except Exception as err:
      return JSONResponse(status_code=500, content={ "error_code": 500, "error_msg": str(err) })