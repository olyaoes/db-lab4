# Import controllers
from my_project.auth.controller.orders.panel_angle_adjustment_controller import PanelAngleAdjustmentController
from my_project.auth.controller.orders.energy_price_controller import EnergyPriceController
from my_project.auth.controller.orders.users_controller import UsersController
from my_project.auth.controller.orders.solar_station_controller import SolarStationController
from my_project.auth.controller.orders.energy_sales_controller import EnergySalesController
from my_project.auth.controller.orders.station_owner_controller import StationOwnerController
from my_project.auth.controller.orders.panel_controller import PanelController
from my_project.auth.controller.orders.battery_controller import BatteryController
from my_project.auth.controller.orders.power_production_controller import PowerProductionController
from my_project.auth.controller.orders.battery_charge_controller import BatteryChargeController

# Initialize controllers
panel_angle_adjustment_controller = PanelAngleAdjustmentController()
energy_price_controller = EnergyPriceController()
users_controller = UsersController()
solar_station_controller = SolarStationController()
energy_sales_controller = EnergySalesController()
station_owner_controller = StationOwnerController()
panel_controller = PanelController()
battery_controller = BatteryController()
power_production_controller = PowerProductionController()
battery_charge_controller = BatteryChargeController()
