from typing import List
from my_project.auth.dao.orders.panel_dao import PanelDAO
from my_project.auth.domain.orders.panel import Panel
from my_project.auth.service.general_service import GeneralService


class PanelService(GeneralService):
    _dao = PanelDAO()

    def create(self, panel: Panel) -> None:
        self._dao.create(panel)

    def get_all_panels(self) -> List[Panel]:
        return self._dao.find_all()

    def get_panels_by_station(self, station_id: int) -> List[Panel]:
        return self._dao.find_by_station_id(station_id)
