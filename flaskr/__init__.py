from flask import Flask
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)

    from flaskr.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from flaskr.auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app


from flaskr import models
