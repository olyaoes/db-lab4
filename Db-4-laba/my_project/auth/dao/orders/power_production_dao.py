from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.power_production import PowerProduction

class PowerProductionDAO(GeneralDAO):
    _domain_type = PowerProduction

    def create(self, production: PowerProduction) -> None:
        self._session.add(production)
        self._session.commit()

    def find_all(self) -> List[PowerProduction]:
        return self._session.query(PowerProduction).all()

    def find_by_panel_id(self, panel_id: int) -> List[PowerProduction]:
        return self._session.query(PowerProduction).filter(PowerProduction.Panel_ID == panel_id).all()

    def find_with_panel(self):
        return (
            self._session.query(PowerProduction)
            .options(
                joinedload(PowerProduction.panel),
            )
            .all()
        )
