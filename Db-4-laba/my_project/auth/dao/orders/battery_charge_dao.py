from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.battery_charge import BatteryCharge

class BatteryChargeDAO(GeneralDAO):
    _domain_type = BatteryCharge

    def create(self, charge: BatteryCharge) -> None:
        self._session.add(charge)
        self._session.commit()

    def find_all(self) -> List[BatteryCharge]:
        return self._session.query(BatteryCharge).all()

    def find_by_battery_id(self, battery_id: int) -> List[BatteryCharge]:
        return self._session.query(BatteryCharge).filter(BatteryCharge.Battery_ID == battery_id).all()

    def find_with_battery(self):
        return (
            self._session.query(BatteryCharge)
            .options(
                joinedload(BatteryCharge.battery),
            )
            .all()
        )
