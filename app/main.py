from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select

from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate


app = FastAPI(
    title="Task Management System",
    description="A REST API for managing tasks",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Welcome to Task Management System"}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db=Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.get("/tasks")
def get_tasks(db=Depends(get_db)):
    result = db.execute(select(Task))
    return result.scalars().all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db=Depends(get_db)):
    result = db.execute(
        select(Task).where(Task.id == task_id)
    )

    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db=Depends(get_db)
):
    result = db.execute(
        select(Task).where(Task.id == task_id)
    )

    existing_task = result.scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_data = task.model_dump()

    for field, value in update_data.items():
        setattr(existing_task, field, value)

    db.commit()
    db.refresh(existing_task)

    return existing_task


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(task_id: int, db=Depends(get_db)):
    result = db.execute(
        select(Task).where(Task.id == task_id)
    )

    existing_task = result.scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(existing_task)
    db.commit()

    return None