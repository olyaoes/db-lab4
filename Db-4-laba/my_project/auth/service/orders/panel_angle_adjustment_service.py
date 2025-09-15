from typing import List
from my_project.auth.dao import PanelAngleAdjustmentDAO
from my_project.auth.domain.orders.panel_angle_adjustment import PanelAngleAdjustment

class PanelAngleAdjustmentService:
    _dao = PanelAngleAdjustmentDAO()

    def create(self, adjustment: PanelAngleAdjustment) -> None:
        self._dao.create(adjustment)

    def get_all_adjustments(self) -> List[PanelAngleAdjustment]:
        return self._dao.find_all()

    def get_adjustments_by_panel_id(self, panel_id: int) -> List[PanelAngleAdjustment]:
        return self._dao.find_by_panel_id(panel_id)
