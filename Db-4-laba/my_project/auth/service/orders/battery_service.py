from typing import List
from my_project.auth.dao import BatteryDAO
from my_project.auth.domain.orders.battery import Battery

class BatteryService:
    _dao = BatteryDAO()

    def create(self, battery: Battery) -> None:
        self._dao.create(battery)

    def get_all_batteries(self) -> List[Battery]:
        return self._dao.find_all()

    def get_battery_by_station_id(self, station_id: int) -> List[Battery]:
        return self._dao.find_by_station_id(station_id)
