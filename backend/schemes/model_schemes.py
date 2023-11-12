from pydantic import BaseModel


class ModelBaseSchema(BaseModel):
    target_name: str
    probability: float
