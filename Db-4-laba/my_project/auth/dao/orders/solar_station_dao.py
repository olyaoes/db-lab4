from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.solar_station import SolarStation

class SolarStationDAO(GeneralDAO):
    _domain_type = SolarStation

    def create(self, station: SolarStation) -> None:
        self._session.add(station)
        self._session.commit()

    def find_all(self) -> List[SolarStation]:
        return self._session.query(SolarStation).all()

    def find_by_owner_id(self, owner_id: int) -> List[SolarStation]:
        return self._session.query(SolarStation).filter(SolarStation.Owner_ID == owner_id).all()

    def find_with_panels(self):
        return (
            self._session.query(SolarStation)
            .options(
                joinedload(SolarStation.panels),
            )
            .all()
        )
