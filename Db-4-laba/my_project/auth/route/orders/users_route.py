from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.users_controller import UsersController
from my_project.auth.domain.orders.users import Users

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.get('')
def get_all_users() -> Response:
    users = UsersController.find_all()
    users_dto = [user.put_into_dto() for user in users]
    return make_response(jsonify(users_dto), HTTPStatus.OK)

@users_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    user = Users.create_from_dto(content)
    UsersController.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@users_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    user = UsersController.find_by_id(user_id)
    if user:
        return make_response(jsonify(user.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)

@users_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = Users.create_from_dto(content)
    try:
        UsersController.update(user_id, user)
        return make_response("User updated", HTTPStatus.OK)
    except ValueError as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND)

@users_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    try:
        UsersController.delete(user_id)
        return make_response("User deleted", HTTPStatus.NO_CONTENT)
    except ValueError as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND)
