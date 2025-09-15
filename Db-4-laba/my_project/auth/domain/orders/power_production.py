from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class PowerProduction(db.Model, IDto):
    __tablename__ = "Power_Production"
    
    Production_ID = db.Column(db.Integer, primary_key=True)  
    Panel_ID = db.Column(db.Integer, nullable=False)  
    Production_Date = db.Column(db.Date, nullable=False) 
    Hour = db.Column(db.Integer, nullable=False) 
    Power_Produced = db.Column(db.Float, nullable=False)  
    def put_into_dto(self) -> Dict[str, Any]:
       
        return {
            "Production_ID": self.Production_ID,
            "Panel_ID": self.Panel_ID,
            "Production_Date": self.Production_Date,
            "Hour": self.Hour,
            "Power_Produced": self.Power_Produced
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PowerProduction:

        return PowerProduction(**dto_dict)
