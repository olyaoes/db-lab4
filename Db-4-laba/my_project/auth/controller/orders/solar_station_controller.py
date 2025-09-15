from typing import List
from my_project.auth.dao.orders.solar_station_dao import SolarStationDAO
from my_project.auth.domain.orders.solar_station import SolarStation

class SolarStationController:
    _dao = SolarStationDAO()

    @staticmethod
    def find_all() -> List[SolarStation]:
        return SolarStationController._dao.find_all()

    @staticmethod
    def create(solar_station: SolarStation) -> None:
        SolarStationController._dao.create(solar_station)

    @staticmethod
    def find_by_owner_id(owner_id: int) -> List[SolarStation]:
        return SolarStationController._dao.find_by_owner_id(owner_id)
