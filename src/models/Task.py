from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.config.db import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks" 

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(255), nullable=False, index=True)
    task_desc = Column(String, nullable=False)
    priority = Column(String(10), nullable=False, default= "low")
    start_date = Column(Date, nullable=False)  
    end_date = Column(Date, nullable=False)
    is_completed = Column(Boolean, default=False)

     # Foreign key to associate with a user
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task(id={self.id}, task_name={self.task_name})"


# # models/Task.py
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship
# from config.db import Base

# class Task(Base):
#     __tablename__ = "tasks"
    
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
    
#     is_completed = Column(Boolean, default=False)
    
   
    
 
