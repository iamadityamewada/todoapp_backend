# from sqlalchemy.orm import Session
# from src.models.user import User
# from src.dtos.user import UserCreate
# from src.core.security import get_password_hash, verify_password, create_access_token

# def create_user(db: Session, user_data: UserCreate):
#     hashed_password = get_password_hash(user_data.password)
#     user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# def authenticate_user(db: Session, username: str, password: str):
#     user = db.query(User).filter(User.username == username).first()
#     if not user or not verify_password(password, user.hashed_password):
#         return False
#     return user
