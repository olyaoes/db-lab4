from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Panel(db.Model, IDto):
    __tablename__ = "Panel"

    Panel_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_id = db.Column(db.Integer, db.ForeignKey("Solar_Station.Station_ID"), nullable=False)
    panel_type = db.Column(db.String(100), nullable=False)
    max_power = db.Column(db.Numeric(10, 2), nullable=True)
    tilt_angle = db.Column(db.Numeric(5, 2), nullable=True)
    panel_efficiency = db.Column(db.Numeric(5, 2), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "Panel_ID": self.Panel_ID,
            "station_id": self.station_id,
            "panel_type": self.panel_type,
            "max_power": str(self.max_power),
            "tilt_angle": str(self.tilt_angle),
            "panel_efficiency": str(self.panel_efficiency),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Panel:
        return Panel(**dto_dict)
