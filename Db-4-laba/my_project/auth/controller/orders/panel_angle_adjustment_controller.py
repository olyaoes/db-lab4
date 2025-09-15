from typing import List
from my_project.auth.dao.orders.panel_angle_adjustment_dao import PanelAngleAdjustmentDAO
from my_project.auth.domain.orders.panel_angle_adjustment import PanelAngleAdjustment

class PanelAngleAdjustmentController:
    _dao = PanelAngleAdjustmentDAO()

    def find_all(self) -> List[PanelAngleAdjustment]:
        return self._dao.find_all()

    def create(self, adjustment: PanelAngleAdjustment) -> None:
        self._dao.create(adjustment)

    def find_by_panel_id(self, panel_id: int) -> List[PanelAngleAdjustment]:
        return self._dao.find_by_panel_id(panel_id)
