import logging
from typing import List
from my_project.auth.dao.orders.station_owner_dao import StationOwnerDAO
from my_project.auth.domain.orders.station_owner import StationOwner

# Налаштовуємо базовий логер
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class StationOwnerController:
    _dao = StationOwnerDAO()

    @staticmethod
    def find_all() -> List[StationOwner]:
        try:
            logging.debug("Attempting to find all station owners.")
            owners = StationOwnerController._dao.find_all()
            logging.debug(f"Found owners: {owners}")
            return owners
        except Exception as e:
            logging.error(f"Error in find_all: {str(e)}")
            raise

    def create(self, station_owner: StationOwner) -> None:
        try:
            logging.debug(f"Attempting to create station owner: {station_owner}")
            self._dao.create(station_owner)
            logging.debug(f"Station owner created successfully: {station_owner}")
        except Exception as e:
            logging.error(f"Error in create: {str(e)}")
            raise

    def find_by_station_id(self, station_id: int) -> List[StationOwner]:
        try:
            logging.debug(f"Attempting to find owners for station with ID {station_id}.")
            owners = StationOwnerController._dao.find_by_station_id(station_id)
            logging.debug(f"Found owners for station {station_id}: {owners}")
            return owners
        except Exception as e:
            logging.error(f"Error in find_by_station_id: {str(e)}")
            raise
