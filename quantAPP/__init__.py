from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from .config import Config
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
login_manager = LoginManager()
toolbar = DebugToolbarExtension()
migrate = Migrate()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    app.app_context().push()

    Bootstrap(app)
    db.init_app(app)
    db.create_all()
    toolbar.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate.init_app(app, db)



    with app.app_context():
        from quantAPP import models
        
        from .routes import asset_portfolio_bp
        app.register_blueprint(asset_portfolio_bp)
        
        from .views import auth_blueprint
        app.register_blueprint(auth_blueprint)
        
        from .home import home_bp
        app.register_blueprint(home_bp)
        
        from .views import home_blueprint
        app.register_blueprint(home_blueprint)
        

        from .views import admin_blueprint
        app.register_blueprint(admin_blueprint, url_prefix='/admin')



        return app

from quantAPP import models
