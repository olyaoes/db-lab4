from typing import List
from my_project.auth.dao import PowerProductionDAO
from my_project.auth.domain.orders.power_production import PowerProduction

class PowerProductionService:
    _dao = PowerProductionDAO()

    def create(self, production: PowerProduction) -> None:
        self._dao.create(production)

    def get_all_productions(self) -> List[PowerProduction]:
        return self._dao.find_all()

    def get_productions_by_station_id(self, station_id: int) -> List[PowerProduction]:
        return self._dao.find_by_station_id(station_id)