from .database import Base 
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
import datetime

# connect model to the table

class Student(Base): 

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)
    college = Column(String)


class Blog(Base): 

    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class Task(Base): 

    __tablename__ = 'dailytasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

