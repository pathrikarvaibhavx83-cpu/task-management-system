from fastapi import Depends, FastAPI
from app.models import Task
from pydantic import BaseModel
from sqlalchemy import select

from app.database import get_db

app = FastAPI()
class TaskCreate(BaseModel):
    title: str 
    description: str | None = None

@app.get("/")
def home():
    return {"message": "Hello from Task Management System"}

@app.get("/tasks")
def get_tasks(db = Depends(get_db)):
    result = db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks

@app.post("/tasks")
def create_task(task: TaskCreate, db = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task