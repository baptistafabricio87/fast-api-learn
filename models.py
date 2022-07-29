"""Create Data Model"""
from pydantic import BaseModel


"""Implementaion from Python 3.10 and above"""
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


"""Implementation from Python 3.6 and above"""
# from typing import Union
# 
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
