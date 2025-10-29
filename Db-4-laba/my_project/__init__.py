import secrets
from typing import Dict, Any
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flasgger import Swagger
from http import HTTPStatus
from my_project.auth.route import register_routes

db = SQLAlchemy()
todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config.update(app_config)
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "connect_args": {
            "ssl": {"ssl_mode": "REQUIRED"}
        }
    }

    _init_db(app)
    register_routes(app)
    _init_swagger(app)
    _init_trigger3_1(app)
    _init_avg_procedure(app)
    create_dynamic_tables_procedure(app)
    return app


def _init_db(app: Flask) -> None:
    db.init_app(app)
    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])
    import my_project.auth.domain
    with app.app_context():
        db.create_all()


def _init_swagger(app: Flask) -> None:
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Solar Station API",
            "description": "API documentation for the Solar Station management system",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": ["http", "https"],
    }
    Swagger(app, template=template)

    @app.route("/hi")
    def hello_world():
        return jsonify({"message": "Hello from Solar Station API!"}), HTTPStatus.OK

    @app.route("/number/<string:todo_id>", methods=["GET", "PUT"])
    def todo_simple(todo_id):
        if todo_id not in todos:
            todos[todo_id] = todo_id
        return jsonify(todos), HTTPStatus.OK


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    pass
