from fastapi import APIRouter
from schemes import *

model_api = APIRouter(prefix='/api/model', tags=['model'])


@model_api.get('', response_model=ModelBaseSchema)
async def get():
    response = {'answer': 'test_answer'}

    return response
