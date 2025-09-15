from typing import List
from my_project.auth.domain.orders.users import Users
from my_project.auth.dao.general_dao import GeneralDAO

class UsersDAO(GeneralDAO):
    _domain_type = Users

    def create(self, user: Users) -> None:
        self._session.add(user)
        self._session.commit()

    def find_all(self) -> List[Users]:
        return self._session.query(Users).all()

    def find_by_id(self, user_id: int) -> Users:
        return self._session.query(Users).filter(Users.user_id == user_id).first()
