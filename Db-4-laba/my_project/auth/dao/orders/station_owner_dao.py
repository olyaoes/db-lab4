import logging
from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.station_owner import StationOwner

# Налаштування базового логера
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class StationOwnerDAO(GeneralDAO):
    _domain_type = StationOwner

    def find_all(self) -> List[StationOwner]:
        try:
            owners = self._session.query(StationOwner).all()
            logging.debug(f"Found owners: {owners}")
            return owners
        except Exception as e:
            logging.error(f"Error in find_all: {str(e)}")
            raise

    def find_by_station_id(self, station_id: int) -> List[StationOwner]:
        try:
            owners = self._session.query(StationOwner).filter(StationOwner.station_id == station_id).all()
            logging.debug(f"Found owners for station {station_id}: {owners}")
            return owners
        except Exception as e:
            logging.error(f"Error in find_by_station_id (station_id={station_id}): {str(e)}")
            raise

    def create(self, station_owner: StationOwner) -> None:
        try:
            logging.debug(f"Attempting to create station owner: {station_owner}")
            self._session.add(station_owner)
            self._session.commit()
            logging.debug(f"Station owner created successfully: {station_owner}")
        except Exception as e:
            logging.error(f"Error in create: {str(e)}")
            self._session.rollback()  # Відкат транзакції у разі помилки
            raise
