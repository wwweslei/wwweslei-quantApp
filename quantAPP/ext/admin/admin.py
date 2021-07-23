from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

admin = Admin()


def init_app(app):
    from quantAPP.ext.db.models import User, Wallet, Company
    from quantAPP.ext.db import db
    admin.name = 'QuantAPP'
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Wallet, db.session))
    admin.add_view(ModelView(Company, db.session))
