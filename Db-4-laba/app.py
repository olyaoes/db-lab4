kkkkkkkk
            if flask_env == DEVELOPMENT:
                config_data = config_data_dict[DEVELOPMENT]
                app = create_app(config_data, additional_config)

                @app.route('/health', methods=['GET'])
                def health():
                    return jsonify({'status': 'ok'})

                @app.route('/example', methods=['GET'])
                def example():
                    return jsonify({'message': 'hello from example'})

                Swagger(app, template=additional_config["SWAGGER"])

                app.run(port=DEVELOPMENT_PORT, debug=True, host="0.0.0.0")

                app.run(host=HOST, port=DEVELOPMENT_PORT, debug=True)

            elif flask_env == PRODUCTION:
                config_data = config_data_dict[PRODUCTION]
                app = create_app(config_data, additional_config)

                @app.route('/health', methods=['GET'])
                def health():
                    return jsonify({'status': 'ok'})

                @app.route('/example', methods=['GET'])
                def example():
                    return jsonify({'message': 'hello from example'})

                Swagger(app, template=additional_config["SWAGGER"])
                serve(app, host=HOST, port=PRODUCTION_PORT)

            else:
                raise ValueError(f"Check OS environment variable '{FLASK_ENV}'")

    except Exception as e:
        print(f"Error loading configuration: {e}")
        raise

if __name__ == '__main__':
    run_flask_app()


