import uvicorn
from routers import *
from fastapi import FastAPI

app = FastAPI()

app.include_router(model_api)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
