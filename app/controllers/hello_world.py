from fastapi import APIRouter

hello_world_routes = APIRouter()


@hello_world_routes.get('/', tags=['hello_world'])
async def hello_world():
    return {'message': 'Hello World!'}


@hello_world_routes.get('/{name}', tags=['hello_world'])
async def hello_name(name: str):
    return {'message': f'Hello {name}!'}
