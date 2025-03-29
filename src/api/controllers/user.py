from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config import db 
from fastapi.requests import Request
from src.dtos.user import UserCreate, UserLogin
from src.api.services.user import UserServices
# from src.core.security import create_access_token


user_router = APIRouter()

user_services = UserServices()

@user_router.post("/signup")
def signup(request:Request, data: UserCreate, db: Session = Depends(db.get_db)):
    return user_services.create_user(request,data,db)


@user_router.post("/login")
def login(request:Request, data: UserLogin, db: Session = Depends(db.get_db)):
    return user_services.login_user(request,data,db)

# @user_router.post("/login")
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = authenticate_user(db, user.username, user.password)
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     access_token = create_access_token({"sub": db_user.username})
#     return {"access_token": access_token, "token_type": "bearer"}
