"""LEARNING FAST API - TUTORIAL USER GUIDE"""

from fastapi import FastAPI, Path, Query

from enums import ModelName
from models import Item, User


app = FastAPI(title="Learn FastAPI")


"""Mix Path, Query n Body parameters"""
@app.put("/items/{item_id}")
def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=1, le=5),
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

"""Multi Body parameters"""
@app.put("/item-user/{item_id}")
def update_item_user(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


"""Path Parameter and Numeric Validations"""
@app.get("/items/{item_id}", status_code=201)
def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=1, le=5),
    q: str,
    # le == less than or equal <=
    # gt == greater than >
    # lt == less than <
    # ge == greater than or equal >= 
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""Query Parameter and String Validations"""
# @app.get("/items/")
# def read_items(
#     item_query: str | None = Query(
#         default=[],
#         alias="item-query",
#         title="Query String", 
#         description="Query strings for the items to search in the database that have a good match",
#         min_length=3,
#         max_length=10,
#         deprecated=True
#     )
# ):
#     results = { "items": [{"item_id": "Foo"}, {"item_id": "Bar"}, {"item_id": "Baz"}] }
#     if item_query:
#         results.update({"item-query": item_query})
#     return results


"""Using Data Model"""
@app.post("/item/new", status_code=201)
def create_item(item: Item):
    return item


@app.post("/items/", status_code=201)
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + (item.price * item.tax)
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

"""Python 3.6 and above"""
# @app.put("/items/{item_id}")
# def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


"""Python 3.10 and above"""
@app.put("/item/{item_id}", status_code=201)
def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/user/me")
def read_user_me():
    return {"user_id":"id current user"}


@app.get("/user/{id}")
def read_user(user_id: str):
    return {"user_id": user_id}


"""# Multiple path and query parameters"""
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(
    user_id: int, item_id: str, short: bool = False, q: str | None = None
):

    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long descrition"}
        )
    return item


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# 
# @app.get("/items/")
# def read_item(skip: int = 0, limit: int = 0):
#     return fake_items_db[skip : skip + limit]


"""# Query Optional Parameter"""
# @app.get("/items/{item_id}")
# def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


"""# Import Union if Python 3.6 and above"""
# from typing import Union
# 


"""# Implementaion for Python 3.6 and above"""
# @app.get("/items/{item_id}")
# def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


"""# Query parameter type conversion"""
# @app.get("/items/{item_id}")
# def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long descrition"}
#         )
#     return item


"""Required query parameters"""
@app.get("/item/{item_id}")
def read_need_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
