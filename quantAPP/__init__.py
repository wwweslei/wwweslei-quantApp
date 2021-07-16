from flask import Flask
from quantAPP.config import Config


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    from quantAPP.ext.auth import login
    login.init_app(app)

    from flask_bootstrap import Bootstrap
    Bootstrap(app)

    from quantAPP.ext.admin import admin
    admin.init_app(app)
    
    from quantAPP.ext import db
    db.init_app(app)


def register_blueprints(app):
    with app.app_context():

        from quantAPP.ext.auth.views import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        from quantAPP.ext.home.views import home_blueprint
        app.register_blueprint(home_blueprint)

        from quantAPP.ext.dashboard.views import dashboard_blueprint
        app.register_blueprint(dashboard_blueprint)

