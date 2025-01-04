from passlib.context import CryptContext


def get_password_hash(password: str) -> str:
    bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return bcrypt.hash(password)
 