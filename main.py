from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

app = FastAPI(
    title="App"
)

class CreateUser(BaseModel):
    email: EmailStr

items = [
    {"id": 1, "name": "item1"},
    {"id": 2, "name": "item2"},
    {"id": 3, "name": "item3"},

]

users = [
    {"id": 1, "name": "item1", "email": ""},
    {"id": 2, "name": "item2", "email": ""},
    {"id": 3, "name": "item3", "email": ""},

]

users1 = [
    {"id": 1, "name": "item1", "email": ""},
    {"id": 2, "name": "item2", "email": ""},
    {"id": 3, "name": "item3", "email": ""},

]

@app.get('/')
def hello():
    return {
        "message": "Hello",
    }

@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}"}
@app.get("/users/list/")
def get_users():
    return users

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
        }

@app.get('/items/')
def list_items():
    return items

@app.get("/items/latest/")
def get_latest_item():
    return items[-1]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item_id == item.get("id"):
            return item
    return ""




