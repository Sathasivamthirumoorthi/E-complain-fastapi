from fastapi import APIRouter,Depends,status,HTTPException,Response

from .. import schemas,models,hashing,database

from sqlalchemy.orm import Session

from ..repository import user

router = APIRouter(
    prefix = "/user",
    tags = ["users"]
)

get_db = database.get_db

@router.post('/',response_model = schemas.ShowUsers)
def create(request : schemas.Users,db : Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/')
def get_all_users(db : Session = Depends(get_db)):
    
    return user.get_all_users(db)

# response_model - schemas

@router.get('/{id}',response_model = schemas.ShowUsers)
def get_all_users(id : int , db : Session = Depends(get_db)):
    return user.user(id,db)

