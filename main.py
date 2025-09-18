from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Learn API")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# # Khai báo router cố định trước router chứa parameter để tránh xung đột
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id":user_id}


# Khi gọi 127.0.0.1:8000/users thì sẽ mặc định in ra ["Rick","Morty"]
# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]


# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]

# class ModelName(str, Enum):
#     alexnet = "alexnet",
#     resnet = "resnet",
#     lenet = "lenet"
    
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# fastapi dev main.py


@app.get("/", status_code=200)
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

class Information(BaseModel):
    name: str
    age: int
    country: str
    
class Item(BaseModel):
    name: str
    description:str | None = None
    price: float
    tax: float | None = None

@app.post("/hello")
def create_item(infor: Information):
    return {"message": f"Hi, {infor.name}!"}


@app.post("/get")
def get_information(infor: Information):
    return {"message": f"Tôi là {infor.name}. Năm nay tôi {infor.age} tuổi. Tôi sống tại {infor.country}"}


@app.post("/items/")
async def tinh_tien(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
        


