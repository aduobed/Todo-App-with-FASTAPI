import sys
sys.path.append("..")

from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from database import models
from datetime import timedelta as time_delta
from database import db_start
from model.model import UserModel as UserMod
from sqlalchemy.orm import Session
from utils.password_hash import get_password_hash
from auth.user_authenticate import authenticate_user
from auth.user_jwt_token_generate import create_access_token
from exceptions.user_token_exception import token_exception

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not Authorized"}},
)

@router.post("/user")
async def create_user(user: UserMod, db: Session = Depends(db_start.get_db)):
    hash_password = get_password_hash(user.password)
    user_todo = models.Users(username=user.username, email=user.email,
                             first_name=user.first_name, last_name=user.last_name, hashed_password=hash_password)

    db.add(user_todo)
    db.commit()
    return {"message": "User created successfully"}

@router.post(" /user/login")
async def get_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(db_start.get_db)):
    user = authenticate_user(form_data.username, form_data.password, db_session)
    if not user:
        return token_exception()

    token_expire_time = time_delta(minutes=20)
    access_token = create_access_token(user.username, user.id, token_expire_time)
    return {"access_token": access_token, "token_type": "bearer"}