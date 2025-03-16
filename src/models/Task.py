from sqlalchemy import Column, Integer, String, Date, Boolean
from src.config.db import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(255), nullable=False, index=True)
    start_date = Column(Date, nullable=False)  
    end_date = Column(Date, nullable=False)
    isCompleted = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"Task(id={self.id}, task_name={self.task_name})"
