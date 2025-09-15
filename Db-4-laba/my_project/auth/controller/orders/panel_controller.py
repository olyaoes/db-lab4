from typing import List  # Додано імпорт List
from my_project import db
from my_project.auth.dao.orders.panel_dao import PanelDAO
from my_project.auth.domain.orders.panel import Panel

class PanelController:
    _dao = PanelDAO()

    @staticmethod
    def find_all() -> List[Panel]:
        return PanelController._dao.find_all()

    @staticmethod
    def create(panel: Panel) -> None:
        PanelController._dao.create(panel)

    @staticmethod
    def find_by_station_id(station_id: int) -> List[Panel]:
        return PanelController._dao.find_by_station_id(station_id)

    @staticmethod
    def delete(panel_id: int) -> None:
        # Шукаємо панель за ID
        panel = Panel.query.get(panel_id)
        if panel:
            # Видаляємо панель
            db.session.delete(panel)
            db.session.commit()
        else:
            raise ValueError(f"Panel with ID {panel_id} not found")
