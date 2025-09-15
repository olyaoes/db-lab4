from typing import List
from my_project.auth.dao.orders.solar_station_dao import SolarStationDAO
from my_project.auth.domain.orders.solar_station import SolarStation
from my_project.auth.service.general_service import GeneralService


class SolarStationService(GeneralService):
    _dao = SolarStationDAO()

    def create(self, solar_station: SolarStation) -> None:
        self._dao.create(solar_station)

    def get_all_stations(self) -> List[SolarStation]:
        return self._dao.find_all()

    def get_stations_by_owner(self, owner_id: int) -> List[SolarStation]:
        return self._dao.find_by_owner_id(owner_id)
