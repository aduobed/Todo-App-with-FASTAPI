from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database import models
from database import db_start
from model.model import UserModel as UserMod
from sqlalchemy.orm import Session
from utils.password_hash import get_password_hash
from auth.user_authenticate import authenticate_user

app = FastAPI()

@app.post("/todo/user")
async def create_user(user: UserMod, db: Session = Depends(db_start.get_db)):
    hash_password = get_password_hash(user.password)
    user_todo = models.Users(username=user.username, email=user.email,
                             first_name=user.first_name, last_name=user.last_name, hashed_password=hash_password)

    db.add(user_todo)
    db.commit()
    return {"message": "User created successfully"}

@app.post("/todo/login")
async def get_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(db_start.get_db)):
    user = authenticate_user(form_data.username, form_data.password, db_session)
    if not user:
        return HTTPException(status_code=400, detail="Incorrect username or password")
    return {"message": "Login successful"}