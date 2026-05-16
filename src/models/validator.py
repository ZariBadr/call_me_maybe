from pydantic import BaseModel
from typing import Dict

class prompt(BaseModel):
    prompt: str


class Parameter(BaseModel):
    type: str


class Return_type(BaseModel):
    type: str


class function_definition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Parameter]
    returns: Return_type
