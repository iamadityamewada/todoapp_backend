from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class TaskDTO(BaseModel):
    task_name: str
    start_date: date
    end_date: Optional[date] = None
    isCompleted: Optional[bool] = False
