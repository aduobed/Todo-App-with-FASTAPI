from fastapi import FastAPI
from database import models
from model.model import UserModel as UserMod
from utils.password_hash import get_password_hash

app = FastAPI()


@app.post("/todo/user")
async def create_user(user: UserMod):
    hash_password = get_password_hash(user.password)
    user_todo = models.Users(username=user.username, email=user.email,
                             first_name=user.first_name, last_name=user.last_name, hashed_password=hash_password)

    return user_todo
