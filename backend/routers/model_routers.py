from fastapi import APIRouter, UploadFile, HTTPException
from schemes import *
from ai import *

model_api = APIRouter(prefix='/api/model', tags=['model'])


@model_api.post('', response_model=ModelBaseSchema)
async def upload(file: UploadFile):
    if not (file.content_type in ['image/png', 'image/jpeg']):
        raise HTTPException(status_code=400, detail='The file must have an extension .jpg or .png')
    answer = prediction(file)
    response = {'target_name': answer[0], 'probability': answer[1]}

    return response
