from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config,BASE_DIR

# creates our app for instantiation
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder='public')
    app.config.from_object(Config)

    db.init_app(app)

    from .main import main as main_blueprint
    from .api import api as api_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app