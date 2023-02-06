from pydantic import BaseModel


# Create initial Pydantic models / schemas¶

# Create an ItemBase and UserBase Pydantic models (or let's say "schemas") to have common attributes while creating or reading data.




class Blog(BaseModel):
    title : str 
    body : str 

class Task(BaseModel):
    title : str
    body : str 

class Student(BaseModel):
    department : str
    college : str 