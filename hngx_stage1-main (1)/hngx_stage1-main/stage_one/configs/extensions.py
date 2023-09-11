"""Extensions setup"""

from flasgger import Swagger
from flask import redirect, url_for
from flask_cors import CORS

from stage_one.configs.swagger import swagger_config, template

def init_app(app):
    """
    The init_app function is a Flask extension initializer.
    It takes the application object as an argument and does the initializations
    of several extensions used.
    The function also returns a tuple of objects that were created or
    initialized, so that we can use them later in our code.

    * app: Create the database and to initialize the swagger documentation
    * return: A tuple of the app, cors and migrate objects
    """

    Swagger(app, config=swagger_config, template=template)
    cors = CORS(app, resources={r"/api*": {"origins": "*"}})

    @app.route("/")
    def default():
        """
        The default function is a redirect to the home.index function, which
        is the base route of our application.
        """
        return redirect("/docs")
    return (app, cors)
