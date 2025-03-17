from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.dtos.user import UserCreate, UserLogin
from src.api.services.user import create_user, authenticate_user
from src.core.security import create_access_token

user_router = APIRouter()

@user_router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return {"message": "User created successfully", "user_id": db_user.id}

@user_router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
