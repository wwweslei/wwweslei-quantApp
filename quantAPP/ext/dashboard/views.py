from flask_login import login_required, current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from quantAPP.ext.profit.profit import stock, info
from quantAPP.ext.db.models import Wallet
from quantAPP.ext.db import db
from .forms import WalletForm
import matplotlib.pyplot as plt
from base64 import b64encode
import yfinance as yf
import io

dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)


def plot():
    df = stock("ciel3")['Close']
    plt.figure()
    df.plot()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    buffer = b''.join(buf)
    b2 = b64encode(buffer).decode('utf-8')
    return b2


@dashboard_blueprint.route('/dashboard/', methods=['GET', 'POST'])
@dashboard_blueprint.route('/dashboard/<ticket>', methods=['GET', 'POST'])
@login_required
def dashboard(ticket=None):
    if ticket:  
        stock = yf.Ticker(ticket+'.sa')
        return render_template(
            'dashboard/details.html',
            title='Detalhe',
            id=id,
            ticket= ticket,
            stock = stock.info
        )
    else:
        wallet_user = current_user.wallets.all()
        return render_template(
            'dashboard/dashboard.html',
            title="Dashboard",
            sunalt=plot(),
            wallet_user=wallet_user
    
        )


@dashboard_blueprint.route('/dashboard/add_position', methods=['GET', 'POST'])
@login_required
def add_position():
    form = WalletForm()
    if form.validate_on_submit():
        position = Wallet(
            ticket=form.ticket.data,
            kind=form.kind.data,
            date=form.date.data,
            amount=form.amount.data,
            price=form.price.data,
            commission=form.commission.data,
            users_id=current_user.get_id()
        )
        db.session.add(position)
        db.session.commit()
        flash('Posição adicionada com sucesso!')
        info(form.ticket.data)
        return redirect(url_for('dashboard_blueprint.dashboard'))

    return render_template(
        'dashboard/wallet_form.html',
        form=form,
        title='Adicionar Posição',
        )

