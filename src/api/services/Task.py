from fastapi.requests import Request
from sqlalchemy.orm import Session
from src.models.Task import Task
from src.middleware.custom_response import send_error, send_success
from src.dtos.Task import TaskDTO
from datetime import datetime
from typing import Optional, List
from sqlalchemy import or_, and_, func
from fastapi.encoders import jsonable_encoder

class TaskServices:
    def create_task(self, request, data, db, current_user):
        try:
            # print("current user", current_user)
            new_task = Task(**dict(data),user_id = current_user)
            db.add(new_task)
            db.commit()
            db.refresh(new_task)
            return send_success(status_code = 201,content=f"Task Created {new_task} ")
        except Exception as e:
            print("create task error : ", e)
            return send_error()
        


    def get_task(self, request, db, current_user):
        try:
            tasks = db.query(Task).all()
            return send_success(status_code=200, content= tasks)
        
        except Exception as e:
            print(f"Error fetching tasks: {e}")
            return send_error(500,message="Failed to fetch tasks", content=str(e))


      
    def delete_task(self, request, id, db, current_user):
        try:
            task = db.query(Task).filter(Task.id == id).first()
            if not task:
                return send_error(404, "Task not found")
            db.delete(task)
            db.commit()
            return send_success(200, content=f"Task Deleted {task}")
        except Exception as e:
            print(f"Error deleting task: {e}")
            return send_error(message="Failed to delete task", content=str(e))  


    def update_task(self, request, data,id, db, current_user):
        try:
            task = db.query(Task).filter(Task.id == id).first()
            if not task:
                return send_error(404, "Task not found")
            task.task_name = data.task_name
            task.task_desc = data.task_desc
            task.start_date = data.start_date
            task.end_date = data.end_date
            task.is_completed = data.is_completed
            db.commit()
            db.refresh(task)
            return send_success(200, content=f"Task Updated{task}")
        except Exception as e:
            print(f"Error updating task: {e}")
            return send_error(message="Failed to update task", content=str(e))


    def filter_tasks(self, request, db ,current_user,
        id: Optional[int] = None,
        task_name: Optional[str] = None, 
        isCompleted: Optional[bool] = None, 
        start_date: Optional[datetime] = None, 
        end_date: Optional[datetime] = None,
        ):
        try:
            query = db.query(Task)
            if id:
                query = query.filter(Task.id == id)

            if task_name:
                query = query.filter(Task.task_name.ilike(f'%{task_name}%'))
            
            if isCompleted is not None:
                query = query.filter(Task.isCompleted == isCompleted)

            if start_date:
                query = query.filter(Task.start_date >= start_date)

            if end_date:
                query = query.filter(Task.end_date <= end_date)
            
            filtered_tasks = query.all()

            
            # task_list = [TaskDTO.from_orm(task).dict() for task in filtered_tasks]
            
            return send_success(200, content=filtered_tasks)

        except Exception as e:
            print(f"Error filtering tasks: {e}")
            return send_error()