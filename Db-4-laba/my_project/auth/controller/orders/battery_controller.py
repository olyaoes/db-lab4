from typing import List
from my_project import db
from my_project.auth.dao.orders.battery_dao import BatteryDAO
from my_project.auth.domain.orders.battery import Battery

class BatteryController:
    _dao = BatteryDAO()

    def find_all(self) -> List[Battery]:
        return self._dao.find_all()

    def create(self, battery: Battery) -> None:
        self._dao.create(battery)

    def find_by_station_id(self, station_id: int) -> List[Battery]:
        return self._dao.find_by_station_id(station_id)

    # Додати метод для пошуку батареї за ID
    def find_by_id(self, battery_id: int) -> Battery:
        battery = Battery.query.get(battery_id)  # Використовуємо SQLAlchemy для пошуку батареї за ID
        return battery

    def update(self, battery_id: int, battery: Battery) -> None:
        existing_battery = Battery.query.get(battery_id)
        if existing_battery:
            existing_battery.Capacity = battery.Capacity
            existing_battery.Usage_Duration = battery.Usage_Duration
            existing_battery.Current_Charge_Level = battery.Current_Charge_Level
            existing_battery.Battery_Type = battery.Battery_Type
            db.session.commit()
        else:
            raise ValueError(f"Battery with ID {battery_id} not found")

    def delete(self, battery_id: int) -> None:
        battery = Battery.query.get(battery_id)
        if battery:
            db.session.delete(battery)
            db.session.commit()
        else:
            raise ValueError(f"Battery with ID {battery_id} not found")
