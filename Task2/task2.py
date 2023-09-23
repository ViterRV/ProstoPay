import asyncio
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_async_session, users

class UserDTO(BaseModel):
    id: Optional[int] = None
    user_name: str
    email: str

class UserAction:
    def __init__(self):
        self.async_db_session = get_async_session()

    async def get(self, user_id: int) -> Optional[UserDTO]:
        async with self.async_db_session as async_db_session:
            user = await async_db_session.execute(users.select().where(users.c.id == user_id))
            user = user.fetchone()
            if user:
                return UserDTO(id=user.id, user_name=user.user_name, email=user.email)
            else:
                return None

    async def add(self, user: UserDTO) -> UserDTO:
        async with self.async_db_session as async_db_session:
            new_user = users.insert().values(user_name=user.user_name, email=user.email)
            result = await async_db_session.execute(new_user)
            await async_db_session.commit()
            return UserDTO(id=result.inserted_primary_key[0], user_name=user.user_name, email=user.email)

async def main():
    user_action = UserAction()

    user_data = UserDTO(user_name="Ruslan", email="Ruslan@example.com")
    added_user = await user_action.add(user_data)
    print("Added User:", added_user)

    get_user = await user_action.get(added_user.id)
    print("Retrieved User:", get_user)

if __name__ == "__main__":
    asyncio.run(main())
