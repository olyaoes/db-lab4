from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response  # Додано Response
from my_project.auth.controller.orders.panel_angle_adjustment_controller import PanelAngleAdjustmentController
from my_project.auth.domain.orders.panel_angle_adjustment import PanelAngleAdjustment

panel_angle_adjustment_bp = Blueprint('panel_angle_adjustment', __name__, url_prefix='/panel_angle_adjustment')

@panel_angle_adjustment_bp.get('')
def get_all_adjustments() -> Response:
    adjustments = PanelAngleAdjustmentController().find_all()
    adjustments_dto = [adjustment.put_into_dto() for adjustment in adjustments]
    return make_response(jsonify(adjustments_dto), HTTPStatus.OK)

@panel_angle_adjustment_bp.post('')
def create_adjustment() -> Response:
    content = request.get_json()
    adjustment = PanelAngleAdjustment.create_from_dto(content)
    PanelAngleAdjustmentController().create(adjustment)
    return make_response(jsonify(adjustment.put_into_dto()), HTTPStatus.CREATED)

@panel_angle_adjustment_bp.get('/<int:panel_id>')
def get_adjustments_by_panel_id(panel_id: int) -> Response:
    adjustments = PanelAngleAdjustmentController().find_by_panel_id(panel_id)
    adjustments_dto = [adjustment.put_into_dto() for adjustment in adjustments]
    return make_response(jsonify(adjustments_dto), HTTPStatus.OK)
