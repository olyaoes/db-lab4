from typing import List
from my_project.auth.dao import StationOwnerDAO
from my_project.auth.domain.orders.station_owner import StationOwner

class StationOwnerService:
    _dao = StationOwnerDAO()

    def create(self, owner: StationOwner) -> None:
        self._dao.create(owner)

    def get_all_owners(self) -> List[StationOwner]:
        return self._dao.find_all()

    def get_owner_by_id(self, owner_id: int) -> StationOwner:
        return self._dao.find_by_id(owner_id)
