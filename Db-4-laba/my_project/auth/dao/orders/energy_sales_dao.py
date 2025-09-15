from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.energy_sales import EnergySales

class EnergySalesDAO(GeneralDAO):
    _domain_type = EnergySales

    def create(self, sale: EnergySales) -> None:
        self._session.add(sale)
        self._session.commit()

    def find_all(self) -> List[EnergySales]:
        return self._session.query(EnergySales).all()

    def find_by_station_id(self, station_id: int) -> List[EnergySales]:
        return self._session.query(EnergySales).filter(EnergySales.Station_ID == station_id).all()

    def find_with_station(self):
        return (
            self._session.query(EnergySales)
            .options(
                joinedload(EnergySales.station),
            )
            .all()
        )
