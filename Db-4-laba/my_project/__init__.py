"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    register_routes(app)
    _init_swagger(app)
    #_init_trigger(app)
    _init_trigger3_1(app)
    _init_avg_procedure(app)  
    create_dynamic_tables_procedure(app)
    return app
def _init_trigger(app: Flask) -> None:
    with app.app_context():
            # Drop the trigger if it exists
            db.session.execute('DROP TRIGGER IF EXISTS trigger_battery_id;')

            # Create the trigger
            db.session.execute('''
            CREATE TRIGGER trigger_battery_id
            BEFORE INSERT ON battery
            FOR EACH ROW
            BEGIN
                IF NEW.Battery_id < 0 THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Primary key (battery_id) cannot be negative';
                END IF;
                                 
            END;
            ''')

def _init_trigger3_1(app: Flask) -> None:
    with app.app_context():
            # Drop the trigger if it exists
            db.session.execute('DROP TRIGGER IF EXISTS prevent_delete_rows;')

            # Create the trigger
            db.session.execute('''
            CREATE TRIGGER prevent_delete_rows
            BEFORE DELETE ON Battery
            FOR EACH ROW
            BEGIN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Deletion of rows is not allowed in the Battery table.';
            END

            ''')  
            db.session.execute('''
            DROP TRIGGER IF EXISTS validate_battery_charge_update;
            CREATE TRIGGER validate_battery_charge_update
            BEFORE UPDATE ON Battery
            FOR EACH ROW
            BEGIN
                IF NEW.Current_Charge_Level > NEW.Capacity THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Charge level cannot exceed battery capacity.';
                END IF;
            END;
        ''')

        # Заборонити додавання записів у таблицю Panel з кутом більше 45
            db.session.execute('''
            DROP TRIGGER IF EXISTS validate_panel_tilt_insert;
            CREATE TRIGGER validate_panel_tilt_insert
            BEFORE INSERT ON Panel
            FOR EACH ROW
            BEGIN
                IF NEW.Tilt_Angle > 45 THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Tilt angle cannot exceed 45 degrees.';
                END IF;
            END;
        ''')

        # Заборонити оновлення Tilt_Angle у таблиці Panel, якщо кут більше 45
            db.session.execute('''
            DROP TRIGGER IF EXISTS validate_panel_tilt_update;
            CREATE TRIGGER validate_panel_tilt_update
            BEFORE UPDATE ON Panel
            FOR EACH ROW
            BEGIN
                IF NEW.Tilt_Angle > 45 THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Tilt angle cannot exceed 45 degrees.';
                END IF;
            END;
        ''')

        # Мінімальна кількість записів у таблиці Users (не менше 6)
            db.session.execute('''
            DROP TRIGGER IF EXISTS enforce_min_users;
            CREATE TRIGGER enforce_min_users
            BEFORE DELETE ON Users
            FOR EACH ROW
            BEGIN
                DECLARE row_count INT;
                SELECT COUNT(*) INTO row_count FROM Users;
                IF row_count <= 6 THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Users table must have at least 6 rows.';
                END IF;
            END;
        ''')

            db.session.commit()
def _init_noname_insert(app: Flask) -> None:
    with app.app_context():
        db.session.execute("""

DROP PROCEDURE IF EXISTS InsertNonameIllnesses;
        CREATE PROCEDURE InsertNonameIllnesses()
        BEGIN
            DECLARE i INT DEFAULT 0;
            DECLARE start_number INT DEFAULT 1000;

            WHILE i < 10 DO
                INSERT INTO illneses (illness_name, treatment_plan)
                VALUES (CONCAT('Noname', start_number + i), 'Treatment plan for Noname');

                SET i = i + 1;
            END WHILE;
        END;
        """)
def _init_avg_procedure(app: Flask) -> None:
    with app.app_context():
        db.session.execute('DROP PROCEDURE IF EXISTS CalculateAveragePrice;')

        db.session.execute("""

                CREATE PROCEDURE CalculateAveragePrice(OUT avg_price DECIMAL(10, 2))
                BEGIN
                    SELECT AVG(Price) INTO avg_price
                    FROM energyprice;
                END;
                                   """)

        db.session.commit() #2e
def create_dynamic_tables_procedure(app: Flask) -> None:

    with app.app_context():
        db.session.execute("""
        DROP PROCEDURE IF EXISTS CreateTablesWithRandomColumns;

        CREATE PROCEDURE CreateTablesWithRandomColumns()
        BEGIN
            DECLARE table_name VARCHAR(128);
            DECLARE done INT DEFAULT 0;

            DECLARE table_cursor CURSOR FOR SELECT DISTINCT id FROM award;
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

            OPEN table_cursor;

            read_loop: LOOP
                FETCH table_cursor INTO table_name;

                IF done THEN
                    LEAVE read_loop;
                END IF;

                SET @dynamic_table_name = CONCAT(table_name, '_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%s'));

                SET @num_columns = FLOOR(1 + RAND() * 9);

                SET @create_table_sql = CONCAT('CREATE TABLE ', @dynamic_table_name, ' (');

                SET @col_index = 1;
                WHILE @col_index <= @num_columns DO
                    SET @col_name = CONCAT('Column_', @col_index);
                    SET @col_type = CASE FLOOR(RAND() * 4)
                        WHEN 0 THEN 'INT'
                        WHEN 1 THEN 'VARCHAR(50)'
                        WHEN 2 THEN 'FLOAT'
                        WHEN 3 THEN 'DATETIME'
                    END;

                    SET @create_table_sql = CONCAT(@create_table_sql, @col_name, ' ', @col_type);

                    IF @col_index < @num_columns THEN
                        SET @create_table_sql = CONCAT(@create_table_sql, ', ');
                    END IF;

                    SET @col_index = @col_index + 1;
                END WHILE;

                SET @create_table_sql = CONCAT(@create_table_sql, ');');

                PREPARE stmt FROM @create_table_sql;
                EXECUTE stmt;
                DEALLOCATE PREPARE stmt;
            END LOOP;

            CLOSE table_cursor;
        END;
        """)
        db.session.commit()
def _init_swagger(app: Flask) -> None:
    # A-lia Swagger
    restx_api = Api(app, title='Pavelchak test backend',
                    description='A simple backend')  # https://flask-restx.readthedocs.io/

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


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    # Get root username and password
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    # Set root username and password in app_config
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass
