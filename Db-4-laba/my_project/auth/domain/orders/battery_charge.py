from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class BatteryCharge(db.Model, IDto):
    __tablename__ = "Battery_Charge"
    
    Charge_ID = db.Column(db.Integer, primary_key=True)  
    Battery_ID = db.Column(db.Integer, db.ForeignKey('Battery.Battery_ID'), nullable=False)
    Charge_Date = db.Column(db.Date, nullable=False)  
    Hour = db.Column(db.Integer, nullable=False)  
    Charge_Level = db.Column(db.Float, nullable=False)  

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "Charge_ID": self.Charge_ID,  
            "Battery_ID": self.Battery_ID,
            "Charge_Date": self.Charge_Date,
            "Hour": self.Hour,
            "Charge_Level": self.Charge_Level
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BatteryCharge:
        return BatteryCharge(**dto_dict)
