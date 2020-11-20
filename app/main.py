import uvicorn
from fastapi import FastAPI

from app.config.settings import settings
from app.controllers.hello_world import hello_world_routes

app = FastAPI()

app.include_router(hello_world_routes, prefix='/hello', tags=['hello_world'])

if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)
