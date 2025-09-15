from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class PanelAngleAdjustment(db.Model, IDto):
    __tablename__ = "Panel_Angle_Adjustment"

    adjustment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    panel_id = db.Column(db.Integer, db.ForeignKey("Panel.Panel_ID"), nullable=False)
    adjustment_date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.Integer, nullable=False)  
    new_angle = db.Column(db.Numeric(5, 2), nullable=True)  

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "adjustment_id": self.adjustment_id,
            "panel_id": self.panel_id,
            "adjustment_date": self.adjustment_date,
            "hour": self.hour,
            "new_angle": str(self.new_angle),  
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PanelAngleAdjustment:
        return PanelAngleAdjustment(**dto_dict)
