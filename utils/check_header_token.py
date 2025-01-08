from fastapi import Header, HTTPException

def check_token(token: str = Header(...)):
    if token != "secret":
        raise HTTPException(status_code=400, detail=" Header token is invalid")