from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.station_owner_controller import StationOwnerController
from my_project.auth.domain.orders.station_owner import StationOwner

# Створюємо Blueprint для маршруту
station_owner_bp = Blueprint('station_owner', __name__, url_prefix='/station_owner')

# Отримати всіх власників станцій
@station_owner_bp.get('')
def get_all_owners() -> Response:
    try:
        owners = StationOwnerController.find_all()
        if not owners:
            return make_response(jsonify({"message": "No owners found"}), HTTPStatus.NOT_FOUND)

        owners_dto = [owner.put_into_dto() for owner in owners]
        return make_response(jsonify(owners_dto), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

# Створити нового власника станції
@station_owner_bp.post('')
def create_station_owner() -> Response:
    try:
        content = request.get_json()

        # Перевіряємо наявність необхідних даних
        if not content or 'station_id' not in content or 'owner_id' not in content:
            return make_response(jsonify({"error": "station_id and owner_id are required"}), HTTPStatus.BAD_REQUEST)

        owner = StationOwner.create_from_dto(content)
        StationOwnerController.create(owner)
        return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

# Отримати власників станції за її ID
@station_owner_bp.get('/station/<int:station_id>')
def get_owners_by_station(station_id: int) -> Response:
    try:
        owners = StationOwnerController.find_by_station_id(station_id)
        if not owners:
            return make_response(jsonify({"message": "No owners found for this station"}), HTTPStatus.NOT_FOUND)

        owners_dto = [owner.put_into_dto() for owner in owners]
        return make_response(jsonify(owners_dto), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

# Видалити власника станції
@station_owner_bp.delete('/remove')
def remove_station_owner() -> Response:
    try:
        content = request.get_json()
        station_id = content.get('station_id')
        owner_id = content.get('owner_id')

        # Перевіряємо, чи є такий запис
        station_owner = StationOwnerController.find_by_station_and_owner(station_id, owner_id)

        if not station_owner:
            return make_response(jsonify({"error": "Owner not found for the station"}), HTTPStatus.NOT_FOUND)

        # Видалення власника
        StationOwnerController.delete(station_owner)

        return make_response(jsonify({"message": "Owner removed from station"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

