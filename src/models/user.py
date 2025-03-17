# # models/User.py
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from src.config.db import Base

# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)
    
#     # One-to-many relationship with tasks 
#     tasks = relationship("Task", back_populates="user")
