from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.panel_controller import PanelController
from my_project.auth.domain.orders.panel import Panel

panel_bp = Blueprint('panel', __name__, url_prefix='/panel')

@panel_bp.get('')
def get_all_panels() -> Response:
    panels = PanelController().find_all()
    panels_dto = [panel.put_into_dto() for panel in panels]
    return make_response(jsonify(panels_dto), HTTPStatus.OK)

@panel_bp.post('')
def create_panel() -> Response:
    content = request.get_json()
    panel = Panel.create_from_dto(content)
    PanelController().create(panel)
    return make_response(jsonify(panel.put_into_dto()), HTTPStatus.CREATED)

@panel_bp.get('/station/<int:station_id>')
def get_panels_by_station(station_id: int) -> Response:
    panels = PanelController().find_by_station_id(station_id)
    panels_dto = [panel.put_into_dto() for panel in panels]
    return make_response(jsonify(panels_dto), HTTPStatus.OK)

@panel_bp.delete('/<int:panel_id>')
def delete_panel(panel_id: int) -> Response:
    try:
        PanelController().delete(panel_id)
        return make_response("Panel deleted", HTTPStatus.NO_CONTENT)
    except ValueError as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND)
