"""
Copyright (c) 2023 - present imitor.com
"""
import os

from flask import Flask

from stage_one.configs.config import configs
from stage_one.configs.extensions import init_app
from stage_one.routes import app_blueprints
from stage_one.utils.utils import Responses

config_name = os.getenv("ENVIRONMENT")


def create_app():
    """
    The create_app function is the entry point for our application.
    It takes no arguments and returns a Flask object that we can use to run
    our app.
    The function does the following:
    * Creates an instance of Flask using __name__ as the argument, which
        tells flask where to look for templates and static files
        (among other things).

    * return: An instance of the flask class
    """
    flask_app = Flask(__name__)
    flask_app.config["JSON_SORT_KEYS"] = False
    flask_app.config.from_object(configs.get(config_name or "development"))
    init_app(flask_app)
    flask_app.register_blueprint(app_blueprints)
    flask_app.register_error_handler(404, Responses.resource_not_found)
    flask_app.register_error_handler(500, Responses.internal_server_error)
    return flask_app


app = create_app()
