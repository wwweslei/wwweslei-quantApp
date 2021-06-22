from flask import Blueprint, render_template
from flask import current_app as app
import pandas as pd
from . import db


# Blueprint Configuration


asset_portfolio_bp = Blueprint(
    'asset_portfolio_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@asset_portfolio_bp.route('/asset_portfolio', methods=['GET'])
def asset_portfolio():
    asset = pd.read_sql_query(
        "SELECT  empresa, cod, Valor, qtde, total FROM asset_portfolio", db.get_engine())
    return render_template(
        'asset_portfolio.html',
        asset=asset,
        title='Asset',
    )
