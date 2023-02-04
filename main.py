from fastapi import FastAPI 


app = FastAPI() 

# decorator 
@app.get('/') 
def index():
    return {'data': {
        'name':'siva'
    }}
 
@app.get('/about') 
def about():
    return {'data': 'about'}