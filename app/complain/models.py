from .database import Base 
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime,ForeignKey
import datetime
from sqlalchemy.orm import relationship


# connect model to the table

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

