from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from .config import Config



db = SQLAlchemy()
toolbar = DebugToolbarExtension()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    toolbar.init_app(app)
    db.init_app(app)


    with app.app_context():
        from .home import home_bp
        from .routes import asset_portfolio_bp
        # from .auth import auth_bp
        db.create_all()

        # Register Blueprints
        # app.register_blueprint(auth_bp)
        # app.register_blueprint(admin.admin_bp)
        app.register_blueprint(home_bp)
        app.register_blueprint(asset_portfolio_bp)

        return app
