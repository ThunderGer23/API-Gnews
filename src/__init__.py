from flask import Flask
from flask_cors import CORS
from .routes import AuthRoutes, GNewsRoutes

app = Flask(__name__)

CORS(app, origins='http://localhost:5000', methods=['GET', 'POST'], allow_headers=['Content-Type'])

def init_app(config):
    """
    The `init_app` function initializes the application with the given configuration and registers the
    blueprints for the `AuthRoutes` and `GNewsRoutes` modules.
    
    :param config: The `config` parameter is an object that contains the configuration settings for the
    application. It is typically a Python module or class that defines various configuration variables
    such as database connection details, secret keys, and other application-specific settings. By
    passing the `config` object to the `app.config.from_object()`
    :return: The `app` object is being returned.
    """
    app.config.from_object(config)
    # blueprints for the `AuthRoutes` and `GNewsRoutes` modules respectively.
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(GNewsRoutes.main, url_prefix='/articles')

    return app
