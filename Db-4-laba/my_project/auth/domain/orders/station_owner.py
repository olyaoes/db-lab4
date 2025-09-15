from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class StationOwner(db.Model, IDto):
    __tablename__ = "Station_Owner"

    station_owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    station_id = db.Column(db.Integer, db.ForeignKey("Solar_Station.Station_ID"), nullable=False)  
    owner_id = db.Column(db.Integer, db.ForeignKey("Users.user_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "station_owner_id": self.station_owner_id,
            "station_id": self.station_id,  
            "owner_id": self.owner_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StationOwner:
        return StationOwner(**dto_dict)

