from fastapi import FastAPI 

from typing import Optional

from pydantic import BaseModel

import uvicorn

app = FastAPI() 

# decorator path get- operation
@app.get('/') 
def index():
    return {'data': {
        'name':'siva'
    }}

@app.get('/blogs')
def blogs(limit=10,published : bool = True):
    if published:
        return {
            'blogs' : f'{limit} published blogs from db'
        }
    else:
        return {
        'blogs' : f'{limit} blogs from db'
        }


@app.get('/blogs/unpublished')
def blog_unpublished():
    return {
        'blogs' : 'unpublished blogs'
    }


@app.get('/blogs/{id}')
def blog(id: int):
    return {
        'blogs' : id
    }

@app.get('/blogs/{id}/commands')
def blog_commands(id: int):
    return {
        id : [
            'sdsadas',
            'sdsadas',
            'sdsadas',

        ]
    }


class Blog(BaseModel):
    title : str 
    body : str
    published_at : Optional[bool]

@app.post('/blog')
def create_blog(request : Blog):
    return {
        'data' : f'Blog is created with title as {request.title}'
    }

# if __name__ == '__main__':
#     uvicorn.run(app,host="127.0.0.1",port = 9000)