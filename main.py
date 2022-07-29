from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user/me")
def read_user_me():
    return {"user_id":"id current user"}


@app.get("/user/{id}")
def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/items/")
def read_item(skip: int = 0, limit: int = 0):
    return fake_items_db[skip : skip + limit]