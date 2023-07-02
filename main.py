from fastapi import FastAPI

from config.database import engine, Base

from middlewares.error_handler import ErrorHandler

from routes import routes

# Crear las tablas de la base de datos.
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = 'Mi primera APP con FastAPI'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

app.include_router(routes, prefix='/api')
  