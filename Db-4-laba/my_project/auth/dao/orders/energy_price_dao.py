from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.energy_price import EnergyPrice

class EnergyPriceDAO(GeneralDAO):
    _domain_type = EnergyPrice

    def create(self, price: EnergyPrice) -> None:
        self._session.add(price)
        self._session.commit()

    def find_all(self) -> List[EnergyPrice]:
        return self._session.query(EnergyPrice).all()

    def find_by_station_id(self, station_id: int) -> List[EnergyPrice]:
        return self._session.query(EnergyPrice).filter(EnergyPrice.Station_ID == station_id).all()

    def find_with_station(self):
        return (
            self._session.query(EnergyPrice)
            .options(
                joinedload(EnergyPrice.station),
            )
            .all()
        )
