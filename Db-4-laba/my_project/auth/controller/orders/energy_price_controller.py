from typing import List
from my_project.auth.dao.orders.energy_price_dao import EnergyPriceDAO
from my_project.auth.domain.orders.energy_price import EnergyPrice
from my_project import db

class EnergyPriceController:
    _dao = EnergyPriceDAO()

    def find_all(self) -> List[EnergyPrice]:
        return self._dao.find_all()

    def create(self, price: EnergyPrice) -> None:
        self._dao.create(price)

    def find_by_date(self, date: str) -> List[EnergyPrice]:
        return self._dao.find_by_date(date)

    def update(self, price_date: str, hour: int, price: EnergyPrice) -> None:
        # Шукаємо запис за датою та годиною
        existing_price = EnergyPrice.query.filter_by(Price_Date=price_date, Hour=hour).first()
        if existing_price:
            # Оновлюємо дані
            existing_price.Price = price.Price
            db.session.commit()
        else:
            raise ValueError(f"Price for date {price_date} and hour {hour} not found")

    def delete(self, price_date: str, hour: int) -> None:
        # Шукаємо запис за датою та годиною
        price = EnergyPrice.query.filter_by(Price_Date=price_date, Hour=hour).first()
        if price:
            # Видаляємо запис
            db.session.delete(price)
            db.session.commit()
        else:
            raise ValueError(f"Price for date {price_date} and hour {hour} not found")
