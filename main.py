from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "hello guys!"

@app.get('/{id}')
def about(id):
    return {'data': id}