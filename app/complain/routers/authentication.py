from datetime import datetime, timedelta

from fastapi import APIRouter,Depends,HTTPException,status

from sqlalchemy.orm import Session 

from .. import schemas,models,hashing,database,token

from fastapi.security import  OAuth2PasswordRequestForm


router = APIRouter(
    tags = ["authenticatons"]
)


@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"invalid credentials")
    
    if not hashing.Hash.verify(request.password,user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"incorrect password")

    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}