from fastapi import APIRouter
from .schemas import CreateUser
from users import crud

router = APIRouter(prefix="/users", tags=["Users"])


users = [
    {"id": 1, "name": "item1", "email": ""},
    {"id": 2, "name": "item2", "email": ""},
    {"id": 3, "name": "item3", "email": ""},

]

@router.get("/list/")
def get_users():
    return users

@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
