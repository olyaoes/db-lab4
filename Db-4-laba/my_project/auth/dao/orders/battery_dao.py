from typing import List
from my_project.auth.domain.orders.battery import Battery
from my_project.auth.dao.general_dao import GeneralDAO

class BatteryDAO(GeneralDAO):
    _domain_type = Battery

    def create(self, battery: Battery) -> None:
        self._session.add(battery)
        self._session.commit()

    def find_all(self) -> List[Battery]:
        return self._session.query(Battery).all()

    def find_by_station_id(self, station_id: int) -> List[Battery]:
        return self._session.query(Battery).filter(Battery.station_id == station_id).all()
