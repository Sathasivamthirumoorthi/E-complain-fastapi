from fastapi import FastAPI

from .complain import schemas,models

from .complain.database import engine,SessionLocal

from sqlalchemy.orm import Session

from .complain.routers import user,authentication


app = FastAPI() 

# if table is not there , it will create one for us
models.Base.metadata.create_all(bind=engine)

# What Is Yield In Python? The Yield keyword in Python is similar to a 
# return statement used for returning values or objects in Python
# def get_db():   
#     db = SessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close()


app.include_router(user.router)


app.include_router(authentication.router)

