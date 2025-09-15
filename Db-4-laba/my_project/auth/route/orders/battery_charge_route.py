from flask import Blueprint, jsonify, request, make_response
from my_project.auth.controller.orders.battery_charge_controller import BatteryChargeController
from my_project.auth.domain.orders.battery_charge import BatteryCharge
from http import HTTPStatus

battery_charge_bp = Blueprint('battery_charge', __name__, url_prefix='/battery_charge')

@battery_charge_bp.get('')
def get_all_battery_charges():
    battery_charges = BatteryChargeController().find_all()
    battery_charges_dto = [battery_charge.put_into_dto() for battery_charge in battery_charges]
    return make_response(jsonify(battery_charges_dto), HTTPStatus.OK)


@battery_charge_bp.post('')
def create_battery_charge():
    content = request.get_json()
    battery_charge = BatteryCharge.create_from_dto(content)
    BatteryChargeController().create(battery_charge)
    return make_response(jsonify(battery_charge.put_into_dto()), HTTPStatus.CREATED)


@battery_charge_bp.get('/<int:battery_id>')
def get_battery_charge_by_battery_id(battery_id: int):
    battery_charges = BatteryChargeController().find_by_battery_id(battery_id)
    battery_charges_dto = [battery_charge.put_into_dto() for battery_charge in battery_charges]
    return make_response(jsonify(battery_charges_dto), HTTPStatus.OK)


@battery_charge_bp.put('/<int:id>')
def update_battery_charge(id: int):
    content = request.get_json()
    
    battery_charge = BatteryCharge.query.get(id)
    
    if not battery_charge:
        return make_response(jsonify({"error": "Battery charge not found"}), HTTPStatus.NOT_FOUND)
    battery_charge.Battery_ID = content.get('Battery_ID', battery_charge.Battery_ID)
    battery_charge.Charge_Date = content.get('Charge_Date', battery_charge.Charge_Date)
    battery_charge.Hour = content.get('Hour', battery_charge.Hour)
    battery_charge.Charge_Level = content.get('Charge_Level', battery_charge.Charge_Level)

    BatteryChargeController().update(battery_charge)
    
    return make_response(jsonify(battery_charge.put_into_dto()), HTTPStatus.OK)
