from typing import List
from my_project.auth.dao.orders.energy_sales_dao import EnergySalesDAO
from my_project.auth.domain.orders.energy_sales import EnergySales

class EnergySalesController:
    _dao = EnergySalesDAO()

    def find_all(self) -> List[EnergySales]:
        return self._dao.find_all()

    def create(self, sale: EnergySales) -> None:
        self._dao.create(sale)

    def find_by_customer_id(self, customer_id: int) -> List[EnergySales]:
        return self._dao.find_by_customer_id(customer_id)
