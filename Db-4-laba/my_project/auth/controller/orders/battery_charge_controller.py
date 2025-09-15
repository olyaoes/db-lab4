from typing import List
from my_project import db
from my_project.auth.dao.orders.battery_charge_dao import BatteryChargeDAO
from my_project.auth.domain.orders.battery_charge import BatteryCharge

class BatteryChargeController:
    _dao = BatteryChargeDAO()

    def find_all(self) -> List[BatteryCharge]:
        return self._dao.find_all()

    def create(self, charge: BatteryCharge) -> None:
        self._dao.create(charge)

    def update(self, battery_charge: BatteryCharge) -> None:
        # Оновлюємо запис за Charge_ID
        existing_battery_charge = BatteryCharge.query.get(battery_charge.Charge_ID)
        if existing_battery_charge:
            # Оновлюємо поля
            existing_battery_charge.Battery_ID = battery_charge.Battery_ID
            existing_battery_charge.Charge_Date = battery_charge.Charge_Date
            existing_battery_charge.Hour = battery_charge.Hour
            existing_battery_charge.Charge_Level = battery_charge.Charge_Level
            # Фіксуємо зміни в базі даних
            db.session.commit()
        else:
            raise ValueError(f"Battery charge with Charge_ID {battery_charge.Charge_ID} not found")

    def find_by_battery_id(self, battery_id: int) -> List[BatteryCharge]:
        return self._dao.find_by_battery_id(battery_id)
