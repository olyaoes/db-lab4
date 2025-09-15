from sqlalchemy import Column, Integer, Float, String, DateTime
from my_project import db

class EnergyPrice(db.Model):
    __tablename__ = 'EnergyPrice'

    Price_ID = db.Column(Integer, primary_key=True)
    Price_Date = db.Column(String(255), nullable=False)  
    Hour = db.Column(Integer, nullable=False)
    Price = db.Column(Float, nullable=False)

    def put_into_dto(self):
        return {
            "Price_ID": self.Price_ID,
            "Price_Date": self.Price_Date,
            "Hour": self.Hour,
            "Price": self.Price,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        return EnergyPrice(**dto_dict)


