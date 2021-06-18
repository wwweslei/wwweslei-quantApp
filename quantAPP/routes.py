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
        title='Flask Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',
    )


asset = pd.read_sql_query(
    "SELECT  empresa, cod, Valor, qtde, total FROM asset_portfolio", db.get_engine())

@asset_portfolio_bp.route('/asset', methods=['GET'])
def asset_portfolio():
    """Assetpage."""
    return render_template(
        'asset_portfolio.html',
        asset = asset
    )
