from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# DTO for Task model
class TaskDTO(BaseModel):
    task_name: str = Field(..., title="Task Name", max_length=255)
    task_desc: str = Field(..., title="Task Description")
    start_date: date = Field(..., title="Start Date")
    end_date: date = Field(..., title="End Date")
    is_completed: Optional[bool] = Field(default=False, title="Is Completed")

    model_config = {
        "from_attributes": True  # This replaces orm_mode in Pydantic v2
    }
