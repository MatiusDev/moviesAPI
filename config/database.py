import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
# Session maker me sirve para enlazar el engine de la base de datos a la ORM
from sqlalchemy.ext.declarative import declarative_base
# Declarative base me permite manipular el ORM

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()