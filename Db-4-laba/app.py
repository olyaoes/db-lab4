import os
from waitress import serve
import yaml
from flasgger import Swagger
from my_project import create_app

DEVELOPMENT_PORT = 1401
PRODUCTION_PORT = 1401
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"

def run_flask_app():
    flask_env = os.getenv(FLASK_ENV, DEVELOPMENT).lower()
    config_yaml_path = os.path.join(os.getcwd(), 'config', 'app.yml')

    try:
        with open(config_yaml_path, "r", encoding='utf-8') as yaml_file:
            config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
            additional_config = config_data_dict[ADDITIONAL_CONFIG]

            if flask_env == DEVELOPMENT:
                config_data = config_data_dict[DEVELOPMENT]
                app = create_app(config_data, additional_config)
                Swagger(app, template=additional_config["SWAGGER"])
                app.run(port=DEVELOPMENT_PORT, debug=True, host="0.0.0.0")

            elif flask_env == PRODUCTION:
                config_data = config_data_dict[PRODUCTION]
                app = create_app(config_data, additional_config)
                Swagger(app, template=additional_config["SWAGGER"])
                serve(app, host=HOST, port=PRODUCTION_PORT)

            else:
                raise ValueError(f"Check OS environment variable '{FLASK_ENV}'")

    except Exception as e:
        print(f"Error loading configuration: {e}")
        raise

if __name__ == '__main__':
    run_flask_app()
