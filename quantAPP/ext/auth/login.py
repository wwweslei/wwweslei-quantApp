from flask_login import LoginManager

login_manager = LoginManager()


def init_app(app):
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
