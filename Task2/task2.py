from typing import Optional

from pydantic import BaseModel
from db import session, User_DB


class UserDTO(BaseModel):
    id: Optional[int] = None
    user_name: str
    email: str

class UserAction:
    def __init__(self):
        self.session = session

    def get(self, user_id: int):
        user = self.session.query(User_DB).filter_by(id=user_id).first()
        if user:
            return UserDTO(id=user.id, user_name=user.user_name, email=user.email)
        else:
            return None

    def add(self, user: UserDTO):
        new_user = User_DB(user_name=user.user_name, email=user.email)
        self.session.add(new_user)
        self.session.commit()
        return UserDTO(id=new_user.id, user_name=new_user.user_name, email=new_user.email)


user_action = UserAction()

user_data = UserDTO(user_name="john_doe", email="john@example.com")
added_user = user_action.add(user_data)

retrieved_user = user_action.get(added_user.id)
print(retrieved_user)