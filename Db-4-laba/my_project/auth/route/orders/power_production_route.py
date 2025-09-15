from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response  # Додано Response
from my_project.auth.controller.orders.power_production_controller import PowerProductionController
from my_project.auth.domain.orders.power_production import PowerProduction

power_production_bp = Blueprint('power_production', __name__, url_prefix='/power_production')

@power_production_bp.get('')
def get_all_productions() -> Response:
    productions = PowerProductionController().find_all()
    productions_dto = [production.put_into_dto() for production in productions]
    return make_response(jsonify(productions_dto), HTTPStatus.OK)

@power_production_bp.post('')
def create_production() -> Response:
    content = request.get_json()
    production = PowerProduction.create_from_dto(content)
    PowerProductionController().create(production)
    return make_response(jsonify(production.put_into_dto()), HTTPStatus.CREATED)

@power_production_bp.get('/<int:station_id>')
def get_productions_by_station_id(station_id: int) -> Response:
    productions = PowerProductionController().find_by_station_id(station_id)
    productions_dto = [production.put_into_dto() for production in productions]
    return make_response(jsonify(productions_dto), HTTPStatus.OK)

