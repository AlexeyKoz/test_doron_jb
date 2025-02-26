from sqlalchemy.orm import Session
from src.dal.role_dal import RoleDAL

class RoleService:
    def __init__(self, db: Session):
        self.role_dal = RoleDAL(db)

    def get_all_roles(self):
        return self.role_dal.get_all_roles()

    def get_role_by_id(self, role_id: int):
        return self.role_dal.get_role_by_id(role_id)

    def create_role(self, name: str):
        existing_role = self.role_dal.get_role_by_id(name)
        if existing_role:
            raise ValueError("Role already exists")
        return self.role_dal.create_role(name)

    def delete_role(self, role_id: int):
        return self.role_dal.delete_role(role_id)
