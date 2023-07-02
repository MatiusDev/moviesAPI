from sqlalchemy import Column, Integer, String, Boolean

from config.database import Base

class User(Base):
  
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  is_active = Column(Boolean)