from fastapi import APIRouter,Depends,status,HTTPException,Response

from sqlalchemy.orm import Session 

from .. import schemas,models,hashing,database



def create(request,db : Session):
    new_user = models.Users(name = request.name,email = request.email , password = hashing.Hash.bcrypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user  

def get_all_users(db : Session):
    users = db.query(models.Users).all()
    return users

def user(id,db : Session):
    user = db.query(models.Users).filter(models.Users.id == id).first() 
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
    return user 