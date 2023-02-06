from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a database URL for SQLAlchemy¶


SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Create the SQLAlchemy engine¶
# But in FastAPI, using normal functions (def) more than one thread could interact with the database for the same request,\
    #  so we need to make SQLite know that it should allow that with

engine = create_engine(SQLALCHEMY_DATABASE_URL,  connect_args={"check_same_thread": False})

# Create a SessionLocal class¶

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Now we will use the function declarative_base() that returns a class.

Base = declarative_base() 