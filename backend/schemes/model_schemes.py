from pydantic import BaseModel


class ModelBaseSchema(BaseModel):
    answer: str
