from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.panel import Panel

class PanelDAO(GeneralDAO):
    _domain_type = Panel

    def create(self, panel: Panel) -> None:
        self._session.add(panel)
        self._session.commit()

    def find_all(self) -> List[Panel]:
        return self._session.query(Panel).all()

    def find_by_station_id(self, station_id: int) -> List[Panel]:
        return self._session.query(Panel).filter(Panel.Station_ID == station_id).all()

    def find_with_power_production(self):
        return (
            self._session.query(Panel)
            .options(
                joinedload(Panel.power_production),
            )
            .all()
        )
