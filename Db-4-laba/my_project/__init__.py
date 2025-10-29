import secrets
from typing import Dict, Any
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
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
    from flask_restx import Api, Resource
    from http import HTTPStatus
    restx_api = Api(app, title='Pavelchak test backend', description='A simple backend')

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, 202
        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    pass
