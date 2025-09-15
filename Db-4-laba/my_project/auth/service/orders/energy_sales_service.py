from typing import List
from my_project.auth.dao import EnergySalesDAO
from my_project.auth.domain.orders.energy_sales import EnergySales

class EnergySalesService:
    _dao = EnergySalesDAO()

    def create(self, sale: EnergySales) -> None:
        self._dao.create(sale)

    def get_all_sales(self) -> List[EnergySales]:
        return self._dao.find_all()

    def get_sales_by_customer_id(self, customer_id: int) -> List[EnergySales]:
        return self._dao.find_by_customer_id(customer_id)
