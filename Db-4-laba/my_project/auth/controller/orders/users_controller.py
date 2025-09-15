from typing import List
from my_project.auth.dao.orders.users_dao import UsersDAO
from my_project.auth.domain.orders.users import Users

class UsersController:
    _dao = UsersDAO()

    @staticmethod
    def find_all() -> List[Users]:
        return UsersController._dao.find_all()

    @staticmethod
    def create(user: Users) -> None:
        UsersController._dao.create(user)

    @staticmethod
    def find_by_id(user_id: int) -> Users:
        return UsersController._dao.find_by_id(user_id)

