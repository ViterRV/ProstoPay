from unittest.mock import patch
import pytest
from task2 import UserAction, UserDTO



@pytest.mark.asyncio
async def test_add_and_get_user():
    user_action = UserAction()
    with patch.object(user_action, 'add', return_value=UserDTO(id=1, user_name="Ruslan", email="Ruslan@example.com")):
        user_data = UserDTO(user_name="Ruslan", email="Ruslan@example.com")
        added_user = await user_action.add(user_data)

        assert added_user.id == 1
        assert added_user.user_name == "Ruslan"
        assert added_user.email == "Ruslan@example.com"

@pytest.mark.asyncio
async def test_get_non_existing_user():
    user_action = UserAction()
    retrieved_user = await user_action.get(999999)
    assert retrieved_user is None

if __name__ == "__main__":
    pytest.main()
