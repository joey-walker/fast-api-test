from random import randint

from fastapi import APIRouter

from app.schemas.user import User

hello_world_routes = APIRouter()


@hello_world_routes.get('/', tags=['hello_world'])
async def hello_world():
    return {'message': 'Hello World!'}


@hello_world_routes.get('/{name}', tags=['hello_world'])
async def hello_name(name: str):
    return {'message': f'Hello {name}!'}


@hello_world_routes.get('/user/{name}', tags=['hello_world'], response_model=User)
async def hello_name(name: str):
    return User(**{'name': name, 'id': randint(0, 1000), 'description': f'This is a description for {name}!'})
