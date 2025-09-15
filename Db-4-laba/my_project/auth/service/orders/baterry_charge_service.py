from typing import List

from my_project.auth.dao import awardDao, childDao
from my_project.auth.dao.orders import (
    KidergartenDao, PositionDao,
    battery_charge_dao, battery_dao, energy_price_dao, energy_sales_dao, panel_angle_adjustment_dao, panel_dao, power_production_dao, solar_station_dao, station_owner_dao, users_dao
)
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import (
    Kindergarten, Position, EmployeeHistory, Users, battery_domain, energy_price_domain, energy_sales_domain, panel_angle_adjustment_domain, panel_domain, power_production_domain, solar_station_domain, station_owner_domain
)


class ChildService(GeneralService):
    _dao = childDao

    def create(self, child: solar_station_domain) -> None:
        self._dao.create(child)

    def get_all_children(self) -> List[solar_station_domain]:
        return self._dao.find_all()

    def get_children_by_last_name(self, last_name: str) -> List[solar_station_domain]:
        return self._dao.find_by_last_name(last_name)
