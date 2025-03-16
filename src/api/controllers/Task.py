from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dtos.Task import TaskDTO
from src.api.services.Task import TaskServices
from fastapi.requests import Request
from src.config import db
from typing import Optional, List
from datetime import datetime

task_router = APIRouter()
task_services = TaskServices()


@task_router.post("/create-task")
def create_task(
    request:Request, data:TaskDTO, db:Session = Depends(db.get_db)
):
    return task_services.create_task(request,data,db)


@task_router.get("/get-task")
def get_task(request:Request, db:Session = Depends(db.get_db)):
    result =  task_services.get_task(request,db)
    return result

@task_router.put("/update-task")
def task_update(
    request:Request ,data:TaskDTO, id:int, db:Session = Depends(db.get_db) 
):
    return task_services.update_task(request,data,id,db)


@task_router.delete("/delete-task")
def delete(
    request:Request,id:int, db:Session = Depends(db.get_db) 
):
    return task_services.delete_task(request,id,db)


@task_router.get("/filter-task")
def filter_tasks(request: Request,
                 id: Optional[int] = None,
                 task_name: Optional[str] = None, 
                 isCompleted: Optional[bool] = None, 
                 start_date: Optional[datetime] = None, 
                 end_date: Optional[datetime] = None, 
                 db: Session = Depends(db.get_db)):
    return task_services.filter_tasks(request, db, id=id, task_name=task_name, isCompleted=isCompleted, start_date=start_date, end_date=end_date)
