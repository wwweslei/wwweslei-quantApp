from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from quantAPP.ext.auth.login import login_manager
from quantAPP.ext.db import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    wallets = db.relationship('Wallet', backref='users', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('A senha não é um atributo legível.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.username}>'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Wallet(db.Model):
    __tablename__ = 'wallets'
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(10), nullable=False)
    kind = db.Column(db.String(10), nullable=False)
    condition = db.Column(db.String(10), default="Open")
    date = db.Column(db.DateTime)
    amount = db.Column(db.Integer)
    price = db.Column(db.Float)
    commission = db.Column(db.Float)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<UserWallet {self.ticket}>"


class Company(db.Model):
    __tablename__ = "companies"
    company = db.Column(db.String(), primary_key=True)
    ticket1 = db.Column(db.String())
    ticket2 = db.Column(db.String())
    ticket3 = db.Column(db.String())
    ticket4 = db.Column(db.String())
    ticket5 = db.Column(db.String())
    ticket6 = db.Column(db.String())
    setor = db.Column(db.String())

def __repr__(self):
    return f"<Company {self.company}>"
