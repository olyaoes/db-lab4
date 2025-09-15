from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller.orders.energy_price_controller import EnergyPriceController
from my_project.auth.domain.orders.energy_price import EnergyPrice

energy_price_bp = Blueprint('energy_price', __name__, url_prefix='/energy_price')

@energy_price_bp.get('')
def get_all_prices() -> Response:
    prices = EnergyPriceController().find_all()
    prices_dto = [price.put_into_dto() for price in prices]
    return make_response(jsonify(prices_dto), HTTPStatus.OK)

@energy_price_bp.post('')
def create_price() -> Response:
    content = request.get_json()
    price = EnergyPrice.create_from_dto(content)
    EnergyPriceController().create(price)
    return make_response(jsonify(price.put_into_dto()), HTTPStatus.CREATED)

@energy_price_bp.get('/<string:date>')
def get_prices_by_date(date: str) -> Response:
    prices = EnergyPriceController().find_by_date(date)
    prices_dto = [price.put_into_dto() for price in prices]
    return make_response(jsonify(prices_dto), HTTPStatus.OK)

@energy_price_bp.put('/<string:price_date>/<int:hour>')
def update_price(price_date: str, hour: int) -> Response:
    content = request.get_json()
    price = EnergyPrice.create_from_dto(content)
    EnergyPriceController().update(price_date, hour, price)
    return make_response("Price updated", HTTPStatus.OK)

@energy_price_bp.delete('/<string:price_date>/<int:hour>')
def delete_price(price_date: str, hour: int) -> Response:
    EnergyPriceController().delete(price_date, hour)
    return make_response("Price deleted", HTTPStatus.NO_CONTENT)

