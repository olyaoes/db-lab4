from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class SolarStation(db.Model, IDto):
    __tablename__ = "Solar_Station"

    
    station_id = db.Column("Station_ID", db.Integer, primary_key=True, autoincrement=True)
    installation_address = db.Column(db.String(255), nullable=False)
    installation_date = db.Column(db.Date, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("Users.user_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "station_id": self.station_id,  
            "installation_address": self.installation_address,
            "installation_date": self.installation_date,
            "owner_id": self.owner_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SolarStation:
        return SolarStation(**dto_dict)

