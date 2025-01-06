from passlib.context import CryptContext


def get_bcrypt() -> CryptContext:
    return CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return get_bcrypt().hash(password)
 
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return get_bcrypt().verify(plain_password, hashed_password)