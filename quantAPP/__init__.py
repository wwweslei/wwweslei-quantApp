from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from .config import Config
from flask_bootstrap import Bootstrap
from quantAPP.ext import db
from quantAPP.ext.admin import admin


login_manager = LoginManager()
toolbar = DebugToolbarExtension()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    app.app_context().push()

    Bootstrap(app)
    db.init_app(app)
    toolbar.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    admin.init_app(app)



    with app.app_context():
        
        from quantAPP.ext.auth.views import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)
  
        from quantAPP.ext.home.views import home_blueprint
        app.register_blueprint(home_blueprint)
        
        from quantAPP.ext.dashboard.views import dashboard_blueprint
        app.register_blueprint(dashboard_blueprint)

        return app

from quantAPP.ext.db import models
