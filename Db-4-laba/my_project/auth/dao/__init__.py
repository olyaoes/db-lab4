"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
# DAO imports for each entity in the solar station project from the 'orders' directory
from .orders.solar_station_dao import SolarStationDAO
from .orders.users_dao import UsersDAO
from .orders.station_owner_dao import StationOwnerDAO
from .orders.panel_dao import PanelDAO
from .orders.battery_dao import BatteryDAO
from .orders.power_production_dao import PowerProductionDAO
from .orders.battery_charge_dao import BatteryChargeDAO
from .orders.energy_sales_dao import EnergySalesDAO
from .orders.panel_angle_adjustment_dao import PanelAngleAdjustmentDAO
from .orders.energy_price_dao import EnergyPriceDAO

# Initialize DAOs for each entity
solarStationDao = SolarStationDAO()
usersDao = UsersDAO()
stationOwnerDao = StationOwnerDAO()
panelDao = PanelDAO()
batteryDao = BatteryDAO()
powerProductionDao = PowerProductionDAO()
batteryChargeDao = BatteryChargeDAO()
energySalesDao = EnergySalesDAO()
panelAngleAdjustmentDao = PanelAngleAdjustmentDAO()
energyPriceDao = EnergyPriceDAO()


