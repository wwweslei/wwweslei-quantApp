from flask_login import login_required, current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from quantAPP.ext.profit.profit import stock, info
from quantAPP.ext.db.models import Wallet
from quantAPP.ext.db import db
from .forms import WalletForm
import matplotlib.pyplot as plt
from base64 import b64encode
import io

dashboard_blueprint = Blueprint("dashboard_blueprint", __name__)


@dashboard_blueprint.route("/dashboard/", methods=["GET", "POST"])
@dashboard_blueprint.route("/dashboard/<ticket>", methods=["GET", "POST"])
@login_required
def dashboard(ticket=None):
    if ticket:
        return render_template(
            "dashboard/details.html",
            title="Detalhe",
            id=id,
            ticket=ticket,
            stock=info(ticket),
            graphic=plot(ticket),
        )
    else:
        return render_template(
            "dashboard/dashboard.html",
            title="Dashboard",
            wallet_user=query_table(),
            zip=zip,
            wallet=query_wallet_distribution(),
        )


@dashboard_blueprint.route("/dashboard/add_position", methods=["GET", "POST"])
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
            classe=form.classe.data,
            users_id=current_user.get_id(),
        )
        db.session.add(position)
        db.session.commit()
        flash("Posição adicionada com sucesso!")
        info(form.ticket.data)
        return redirect(url_for("dashboard_blueprint.dashboard"))

    return render_template(
        "dashboard/wallet_form.html",
        form=form,
        title="Adicionar Posição",
    )


def plot(ticket):
    df = stock(ticket)["Close"]
    plt.figure()
    df.plot()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    buffer = b"".join(buf)
    graphic = b64encode(buffer).decode("utf-8")
    return graphic


def query_table():
    stmt = f"""
        SELECT 
            id,
            ticket,
            kind,
            condition,
            date,
            sum(w.amount) as amount,
            sum(w.price)/COUNT(w.ticket) as price,
            classe,
            users_id
        from wallets w
            where w.users_id == {current_user.id}
            and w.condition == 'Open'
        group by w.ticket
    """
    query = [
        {column: value for column, value in rowproxy.items()}
        for rowproxy in db.session.execute(stmt).fetchall()
    ]

    query_info = [info(stock["ticket"]).to_dict("records")[0] for stock in query]

    query_stock_value = [
        round(float(stock(ticket["ticket"]).tail(1)["Close"]), 2) for ticket in query
    ]

    return query, query_info, query_stock_value


def query_wallet_distribution():
    wallet = {
        "FII": 0,
        "BDR": 0,
        "ETF": 0,
        "AÇÃO": 0,
    }
    table = query_table()
    for stock_value, classe in zip(table[2], table[0]):
        wallet[classe["classe"]] += classe["amount"] * stock_value
    return wallet
