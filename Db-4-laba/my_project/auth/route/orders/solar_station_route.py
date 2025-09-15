from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.solar_station_controller import SolarStationController
from my_project.auth.domain.orders.solar_station import SolarStation

solar_station_bp = Blueprint('solar_station', __name__, url_prefix='/solar_station')

@solar_station_bp.get('')
def get_all_stations() -> Response:
    stations = SolarStationController.find_all()
    stations_dto = [station.put_into_dto() for station in stations]
    return make_response(jsonify(stations_dto), HTTPStatus.OK)

@solar_station_bp.post('')
def create_station() -> Response:
    content = request.get_json()
    station = SolarStation.create_from_dto(content)
    SolarStationController.create(station)
    return make_response(jsonify(station.put_into_dto()), HTTPStatus.CREATED)

@solar_station_bp.get('/owner/<int:owner_id>')
def get_stations_by_owner(owner_id: int) -> Response:
    stations = SolarStationController.find_by_owner_id(owner_id)
    stations_dto = [station.put_into_dto() for station in stations]
    return make_response(jsonify(stations_dto), HTTPStatus.OK)
