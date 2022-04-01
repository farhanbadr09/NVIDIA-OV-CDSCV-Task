import os
from flask import Flask, current_app, render_template


def create_app() -> Flask:
    """Flask app factory.
    Loads configuration for database connections, routes, secrets, etc.
    """
    app = Flask(__name__, instance_relative_config=False)

    if os.getenv("FLASK_ENV") == "production":
        app.config.from_object("minipaste.app.config.ProdConfig")

    # use in memory sqlite db for dev
    if os.getenv("FLASK_ENV") == "development":
        app.config.from_object("minipaste.app.config.DevConfig")

    with app.app_context():
        from .api import api
        from .commands import database_bp

        app.register_blueprint(api, url_prefix="/api")
        app.register_blueprint(database_bp)

    return app
