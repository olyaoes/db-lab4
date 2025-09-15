from typing import List
from my_project.auth.dao.orders.power_production_dao import PowerProductionDAO
from my_project.auth.domain.orders.power_production import PowerProduction

class PowerProductionController:
    _dao = PowerProductionDAO()

    def find_all(self) -> List[PowerProduction]:
        return self._dao.find_all()

    def create(self, production: PowerProduction) -> None:
        self._dao.create(production)

    def find_by_station_id(self, station_id: int) -> List[PowerProduction]:
        return self._dao.find_by_station_id(station_id)
