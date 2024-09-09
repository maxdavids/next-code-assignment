from pydantic import BaseModel

class CreateUserProperties(BaseModel):
    username: str
    password: str

class CreateTaskProperties(BaseModel):
    title: str
    description: str
    date: str
    isCompleted: bool
    isImportant: bool

class UserModel(BaseModel):
    id: str
    username: str
    hashed_password: str

class TaskModel(BaseModel):
    id: str
    userId: str
    title: str
    description: str
    date: str
    isCompleted: bool
    isImportant: bool
