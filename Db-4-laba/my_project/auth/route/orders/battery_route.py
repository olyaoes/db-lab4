from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.battery_controller import BatteryController
from my_project.auth.domain.orders.battery import Battery

battery_bp = Blueprint('battery', __name__, url_prefix='/battery')

@battery_bp.get('')
def get_all_batteries() -> Response:
    batteries = BatteryController().find_all()
    batteries_dto = [battery.put_into_dto() for battery in batteries]
    return make_response(jsonify(batteries_dto), HTTPStatus.OK)
@battery_bp.get('/<int:battery_id>')
def get_battery_with_charges(battery_id: int) -> Response:
    battery = BatteryController().find_by_id(battery_id)
    
    if not battery:
        return make_response({"error": f"Battery with ID {battery_id} not found"}, HTTPStatus.NOT_FOUND)
    
    return make_response(jsonify(battery.put_into_dto()), HTTPStatus.OK)


@battery_bp.post('')
def create_battery() -> Response:
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    BatteryController().create(battery)
    return make_response(jsonify(battery.put_into_dto()), HTTPStatus.CREATED)

@battery_bp.get('/station/<int:station_id>')
def get_batteries_by_station(station_id: int) -> Response:
    batteries = BatteryController().find_by_station_id(station_id)
    batteries_dto = [battery.put_into_dto() for battery in batteries]
    return make_response(jsonify(batteries_dto), HTTPStatus.OK)

@battery_bp.put('/<int:battery_id>')
def update_battery(battery_id: int) -> Response:
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    
    try:
        BatteryController().update(battery_id, battery)
        return make_response(jsonify(battery.put_into_dto()), HTTPStatus.OK)
    except ValueError:
        return make_response({"error": f"Battery with ID {battery_id} not found"}, HTTPStatus.NOT_FOUND)

@battery_bp.delete('/<int:battery_id>')
def delete_battery(battery_id: int) -> Response:
    try:
        BatteryController().delete(battery_id)
        return make_response("Battery deleted", HTTPStatus.NO_CONTENT)
    except ValueError:
        return make_response({"error": f"Battery with ID {battery_id} not found"}, HTTPStatus.NOT_FOUND)
