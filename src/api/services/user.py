from sqlalchemy.orm import Session
from src.models.user import User
from src.middleware.custom_response import send_error, send_success
from src.dtos.user import UserCreate
from src.core.security import get_password_hash, verify_password, create_access_token

class UserServices:
    def create_user(self,request, data, db):
        try:
            existing_user = db.query(User).filter((User.username == data.username) or (User.email == data.email)).first()
            if existing_user:
                        return send_error(status_code=400, message="User already exists with the same email or username", content = [existing_user.username, existing_user.email])
                
            hashed_password = get_password_hash(data.password)
            user = User(username=data.username, email=data.email, password=hashed_password)
            print(user.username, user.email, user.password, user.tasks)
            db.add(user)
            db.commit()
            db.refresh(user)
            return send_success(status_code=201, content = [{"username":user.username},{"email":user.email}])
        except Exception as e:
            print("Error : ", e)
            return send_error(status_code=500)
        
    def login_user(self,request,data,db):
          try:
                user = db.query(User).filter(User.username == data.username).first()

                if not user:
                      return send_error(status_code=404)
                
                if not verify_password(data.password, user.password):
                      return send_error(status_code=401)
                
                access_token = create_access_token(data={"sub": user.id})

                return send_success(status_code=200, content=[{"access_token":access_token}, {"token_type": "bearer"}])
          except Exception as e:
                print("Error in Login :", e)
                return send_error(status_code=500)       

    # def authenticate_user(db: Session, username: str, password: str):
    #     try:
    #         user = db.query(User).filter(User.username == username).first()
    #         if not user or not verify_password(password, user.hashed_password):
    #             return False
    #         return user 
    #     except:
    #          send_error() 
