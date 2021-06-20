from flask import Blueprint, render_template
from flask import current_app as app
import pandas as pd
from . import db


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

asset_portfolio_bp = Blueprint(
    'asset_portfolio_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    return render_template(
        'index.html',
        title='Dashboard',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',
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
