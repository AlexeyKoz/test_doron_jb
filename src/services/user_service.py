from sqlalchemy.orm import Session
from src.dal.user_dal import UserDAL

class UserService:
    def __init__(self, db: Session):
        self.user_dal = UserDAL(db)

    def get_all_users(self):
        return self.user_dal.get_all_users()

    def get_user_by_id(self, user_id: int):
        return self.user_dal.get_user_by_id(user_id)

    def create_user(self, first_name: str, last_name: str, email: str, password: str, role_id: int):
        existing_user = self.user_dal.get_user_by_id(email)
        if existing_user:
            raise ValueError("User with this email already exists")
        return self.user_dal.create_user(first_name, last_name, email, password, role_id)

    def delete_user(self, user_id: int):
        return self.user_dal.delete_user(user_id)
