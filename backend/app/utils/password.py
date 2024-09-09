from passlib.context import CryptContext

def get_password_context() -> CryptContext:
    return CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def get_password_hash(password: str, pwd_context: CryptContext) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str, pwd_context: CryptContext) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
