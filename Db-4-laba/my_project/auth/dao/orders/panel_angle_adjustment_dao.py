from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.panel_angle_adjustment import PanelAngleAdjustment

class PanelAngleAdjustmentDAO(GeneralDAO):
    _domain_type = PanelAngleAdjustment

    def create(self, adjustment: PanelAngleAdjustment) -> None:
        self._session.add(adjustment)
        self._session.commit()

    def find_all(self) -> List[PanelAngleAdjustment]:
        return self._session.query(PanelAngleAdjustment).all()

    def find_by_panel_id(self, panel_id: int) -> List[PanelAngleAdjustment]:
        return self._session.query(PanelAngleAdjustment).filter(PanelAngleAdjustment.Panel_ID == panel_id).all()

    def find_with_panel(self):
        return (
            self._session.query(PanelAngleAdjustment)
            .options(
                joinedload(PanelAngleAdjustment.panel),
            )
            .all()
        )
