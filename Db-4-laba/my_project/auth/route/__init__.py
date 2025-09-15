"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each of your specific entities
    from .orders.panel_angle_adjustment_route import panel_angle_adjustment_bp
    from .orders.energy_price_route import energy_price_bp
    from .orders.users_route import users_bp
    from .orders.solar_station_route import solar_station_bp
    from .orders.energy_sales_route import energy_sales_bp
    from .orders.station_owner_route import station_owner_bp
    from .orders.panel_route import panel_bp
    from .orders.battery_route import battery_bp
    from .orders.power_production_route import power_production_bp
    from .orders.battery_charge_route import battery_charge_bp

    # Register each blueprint with the app
    app.register_blueprint(panel_angle_adjustment_bp)
    app.register_blueprint(energy_price_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(solar_station_bp)
    app.register_blueprint(energy_sales_bp)
    app.register_blueprint(station_owner_bp)
    app.register_blueprint(panel_bp)
    app.register_blueprint(battery_bp)
    app.register_blueprint(power_production_bp)
    app.register_blueprint(battery_charge_bp)
