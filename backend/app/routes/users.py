from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models import UserModel, CreateUserProperties
from app.utils.password import get_password_hash, get_password_context, verify_password
from app.utils.token import create_access_token
from app.utils.mockdb import get_users

router = APIRouter(prefix = "/api")

users_db = get_users()

def get_pwd_context():
    return get_password_context()

@router.post("/users/")
async def create_user(user: CreateUserProperties, pwd_context = Depends(get_pwd_context)):
    if user.username in users_db:
        raise HTTPException(status_code = 400, detail = "Username already registered")

    user_id = str(len(users_db) + 1)
    hashed_password = get_password_hash(user.password, pwd_context)

    new_user = UserModel(
        id = user_id,
        username = user.username,
        hashed_password = hashed_password
    )

    users_db[user.username] = new_user

    return { "message": "User created successfully" }

@router.post("/login/")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), pwd_context = Depends(get_pwd_context)):
    user = users_db.get(form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password, pwd_context):
        raise HTTPException(status_code = 400, detail = "Incorrect username or password")

    access_token = create_access_token(data = { "sub": user.username })

    return { "access_token": access_token, "token_type": "bearer" }
