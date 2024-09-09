from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.models import UserModel
from app.utils.password import get_password_hash, get_password_context

users_db = {}
tasks_db = []

pwd_context = get_password_context()

# hard-coded user
user_id = '1'
username = 'test'
password = 'test'
hashed_password = get_password_hash(password, pwd_context)

new_user = UserModel(
    id = user_id,
    username = username,
    hashed_password = hashed_password
)

users_db[new_user.username] = new_user

def get_users():
    return users_db

def get_tasks():
    return tasks_db
