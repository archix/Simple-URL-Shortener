from config import config, SELECTED_CONFIG
from flask import Flask
from flask_migrate import Migrate
from shortener.controllers import shortener

from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[SELECTED_CONFIG])

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register the blueprints
    app.register_blueprint(shortener)

    return app
