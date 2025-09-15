"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Імпорти сервісів
from .orders.power_production_service import PowerProductionService
from .orders.baterry_charge_service import BatteryChargeService
from .orders.panel_angle_adjustment_service import PanelAngleAdjustmentService
from .orders.energy_price_service import EnergyPriceService
from .orders.users_service import UsersService
from .orders.baterry_charge_service import BatteryService
from .orders.energy_sales_service import EnergySalesService
from .orders.solar_station_service import SolarStationService
from .orders.station_owner_service import StationOwnerService
from .orders.panel_service import PanelService
from .orders.energy_price_service import EnergyPriceService
from .orders.battery_service import BatteryService

# Ініціалізація сервісів
powerProductionService = PowerProductionService()
batteryChargeService = BatteryChargeService()
panelAngleAdjustmentService = PanelAngleAdjustmentService()
energyPriceService = EnergyPriceService()
usersService = UsersService()
batteryService = BatteryService()
energySalesService = EnergySalesService()
solarStationService = SolarStationService()
stationOwnerService = StationOwnerService()
panelService = PanelService()
energyPriceService = EnergyPriceService()
batteryService = BatteryService()
