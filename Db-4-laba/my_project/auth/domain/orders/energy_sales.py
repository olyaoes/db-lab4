from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class EnergySales(db.Model, IDto):
    __tablename__ = "Energy_Sales"
    
 
    Sale_ID = db.Column(db.Integer, primary_key=True)  
    station_id = db.Column(db.Integer, db.ForeignKey('Solar_Station.Station_ID'), nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    energy_sold = db.Column(db.Float, nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "Sale_ID": self.Sale_ID,  
            "station_id": self.station_id,
            "sale_date": self.sale_date,
            "hour": self.hour,
            "energy_sold": self.energy_sold,
            "price_per_unit": self.price_per_unit
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EnergySales:
        return EnergySales(**dto_dict)
