from __future__ import annotations
from typing import Dict, Any, List
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Battery(db.Model, IDto):
    __tablename__ = "Battery"
    
    Battery_ID = db.Column(db.Integer, primary_key=True)  
    Station_ID = db.Column(db.Integer, nullable=False)  
    Capacity = db.Column(db.Float, nullable=False)  
    Usage_Duration = db.Column(db.Float, nullable=True)  
    Current_Charge_Level = db.Column(db.Float, nullable=True)  
    Battery_Type = db.Column(db.String(255), nullable=True)
    
    # Відношення до BatteryCharge
    charges = db.relationship('BatteryCharge', backref='battery', lazy=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "Battery_ID": self.Battery_ID,
            "Station_ID": self.Station_ID,
            "Capacity": self.Capacity,
            "Usage_Duration": self.Usage_Duration,
            "Current_Charge_Level": self.Current_Charge_Level,
            "Battery_Type": self.Battery_Type,
            "Charges": [charge.put_into_dto() for charge in self.charges] if self.charges else []
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Battery:
        return Battery(**dto_dict)
