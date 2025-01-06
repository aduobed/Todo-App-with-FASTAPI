from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from exceptions.user_token_exception import user_exception, token_exception

secret_key = "secret_key"
algorithm = "HS256"

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(username: str, user_id: str, time_delta: [Optional[timedelta]] = None):
    if time_delta:
        expire = datetime.utcnow() + time_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {"sub": username, "user_id": user_id, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        user_id: str = payload.get("user_id")
        if username is None or user_id is None:
            raise user_exception()
    except JWTError:
        raise user_exception()
    return {"username": username, "user_id": user_id}