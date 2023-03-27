from pydantic import BaseModel

from typing import List,Optional

# Create initial Pydantic models / schemas¶

# Create an ItemBase and UserBase Pydantic models (or let's say "schemas") to have common attributes while creating or reading data.



class Users(BaseModel):
    name : str 
    email : str
    password : str 
    

class ShowUsers(BaseModel):
    name : str 
    email : str

    class Config():
        orm_mode = True
    
class Login(BaseModel):
    username : str
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
