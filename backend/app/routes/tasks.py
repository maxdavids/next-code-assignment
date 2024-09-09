from fastapi import APIRouter, HTTPException, Depends
from app.models import TaskModel, CreateTaskProperties
from app.utils.mockdb import get_tasks
from app.utils.token import get_current_user

router = APIRouter(prefix = "/api")

tasks_db = get_tasks()

@router.get("/tasks/")
async def get_tasks(current_user: dict = Depends(get_current_user)):
    return tasks_db

@router.get("/tasks/{task_id}")
async def get_single_task(task_id: int, current_user: dict = Depends(get_current_user)):
    task = tasks_db.get(task_id)

    if not task:
        raise HTTPException(status_code = 400, detail = "Incorrect task_id")

    return { "task": task }

@router.post("/tasks/")
async def create_task(task: CreateTaskProperties, current_user: dict = Depends(get_current_user)):
    task_id = str(len(tasks_db) + 1)

    new_task = TaskModel(
        id = task_id,
        userId = current_user.id,
        title = task.title,
        description = task.description,
        date = task.date,
        isCompleted = task.isCompleted,
        isImportant = task.isImportant
    )

    tasks_db.append(new_task)

    return { "message": "Task created", "task": new_task }

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: dict = Depends(get_current_user)):
    remove_id = str(task_id)
    index = next((i for i, task in enumerate(tasks_db) if task.id == remove_id), -1)

    if index >= 0:
        del tasks_db[index]

    return { "message": f"Task with id {remove_id} deleted" }
