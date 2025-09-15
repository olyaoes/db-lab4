from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response  # Додано Response
from my_project.auth.controller.orders.energy_sales_controller import EnergySalesController
from my_project.auth.domain.orders.energy_sales import EnergySales

energy_sales_bp = Blueprint('energy_sales', __name__, url_prefix='/energy_sales')

@energy_sales_bp.get('')
def get_all_sales() -> Response:
    sales = EnergySalesController().find_all()
    sales_dto = [sale.put_into_dto() for sale in sales]
    return make_response(jsonify(sales_dto), HTTPStatus.OK)

@energy_sales_bp.post('')
def create_sale() -> Response:
    content = request.get_json()
    sale = EnergySales.create_from_dto(content)
    EnergySalesController().create(sale)
    return make_response(jsonify(sale.put_into_dto()), HTTPStatus.CREATED)

@energy_sales_bp.get('/<int:customer_id>')
def get_sales_by_customer_id(customer_id: int) -> Response:
    sales = EnergySalesController().find_by_customer_id(customer_id)
    sales_dto = [sale.put_into_dto() for sale in sales]
    return make_response(jsonify(sales_dto), HTTPStatus.OK)
