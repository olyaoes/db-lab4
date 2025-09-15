from typing import List, Optional
from my_project.auth.dao.orders.energy_price_dao import EnergyPrice
from my_project.auth.dao.orders.energy_price_dao import EnergyPriceDAO
from my_project.auth.service.general_service import GeneralService


class EnergyPriceService(GeneralService):
    def __init__(self):
        self._dao = EnergyPriceDAO()

    def create_price(self, price: EnergyPrice) -> None:
        self._dao.create(price)

    def get_all_prices(self) -> List[EnergyPrice]:
        return self._dao.find_all()

    def get_price_by_id(self, price_id: int) -> Optional[EnergyPrice]:
        return self._dao.find_by_id(price_id)

    def update_price(self, price: EnergyPrice) -> None:
        self._dao.update(price)

    def delete_price(self, price_id: int) -> None:
        self._dao.delete(price_id)
