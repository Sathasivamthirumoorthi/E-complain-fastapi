from fastapi import FastAPI,Depends,status,Response,HTTPException

from . import schemas,models

from .database import engine,SessionLocal

from sqlalchemy.orm import Session


app = FastAPI() 

# if table is not there , it will create one for us
models.Base.metadata.create_all(bind=engine)

# What Is Yield In Python? The Yield keyword in Python is similar to a 
# return statement used for returning values or objects in Python
def get_db():   
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()



@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog,db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body= request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


@app.post('/task')
def create_task(request : schemas.Task,db : Session = Depends(get_db)):
    new_task = models.Task(title=request.title,body=request.body)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.post('/student')
def create_student(request : schemas.Student,db : Session = Depends(get_db)):
    new_student = models.Student(department=request.department,college=request.college)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get('/blogs')
def get_all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blogs/{id}',status_code=200)
def get_blog_by_id(id,response : Response ,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with this id {id} not found ")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':'Not found'}
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def get_blog_by_id(id,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
    db.delete()

