from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from .forms import LoginForm, RegistrationForm
from quantAPP.ext.db import db
from quantAPP.ext.db.models import User
from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Você se registrou com sucesso! Agora você pode fazer o login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            login_user(user)

            return redirect(url_for('dashboard_blueprint.dashboard'))

        else:
            flash('E-mail ou senha inválidos.')

    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi deslogado com sucesso.')

    return redirect(url_for('auth.login'))
