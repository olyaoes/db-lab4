from typing import List
from my_project.auth.dao import UsersDAO
from my_project.auth.domain.orders.users import Users

class UsersService:
    _dao = UsersDAO()

    def create(self, user: Users) -> None:
        self._dao.create(user)

    def get_all_users(self) -> List[Users]:
        return self._dao.find_all()

    def get_user_by_id(self, user_id: int) -> Users:
        return self._dao.find_by_id(user_id)

