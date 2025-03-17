# from src.models.user import User
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from fastapi import Depends, HTTPException
# from jose import JWTError, jwt
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from src.config.db import get_db
# from src.models.user import User

# SECRET_KEY = "your-secret-key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=401, detail="Could not validate credentials"
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: int = payload.get("sub")
#         if user_id is None:
#             raise credentials_exception
#         user = db.query(User).filter(User.id == user_id).first()
#         if user is None:
#             raise credentials_exception
#         return user.id
#     except JWTError:
#         raise credentials_exception
    

# # # core/security.py
# # from fastapi import Depends, HTTPException
# # from jose import JWTError, jwt
# # from fastapi.security import OAuth2PasswordBearer
# # from sqlalchemy.orm import Session
# # from src.config.db import get_db
# # from src.models.user import User

# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

# # SECRET_KEY = "your_secret_key"
# # ALGORITHM = "HS256"

# # def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
# #     credentials_exception = HTTPException(
# #         status_code=401, detail="Could not validate credentials"
# #     )
# #     try:
# #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
# #         user_id: int = payload.get("sub")
# #         if user_id is None:
# #             raise credentials_exception
# #         user = db.query(User).filter(User.id == user_id).first()
# #         if user is None:
# #             raise credentials_exception
# #         return user.id
# #     except JWTError:
# #         raise credentials_exception


