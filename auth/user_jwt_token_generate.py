from datetime import datetime, timedelta
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

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
