"""Create Data Model"""
from pydantic import BaseModel, Field
from typing import List

"""Implementaion in Python 3.10 and above"""
class Image(BaseModel):
    url: str
    name: str


class User(BaseModel):
    user_id: int
    username: str
    full_name: str | None = None

    
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="Description of item", max_length=300
    )
    price: float = Field(
        gt=0, description="Price must be greater than zero"
    )
    tax: float | None = None
    tag: set[str] = set()
    image: Image | None = None
    user: User | None = None     

    
"""Implementation in Python 3.6 and above"""
# from typing import Union
#_
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#_
# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None
