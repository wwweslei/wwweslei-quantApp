import io
from base64 import b64encode
from flask import Blueprint, render_template
from flask import current_app as app
import yfinance as yf
import matplotlib.pyplot as plt

# Blueprint Configuration
def plot():
    df = yf.download("petr4.sa")['Close']
    plt.figure()
    df.plot()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    buffer = b''.join(buf)
    b2 = b64encode(buffer).decode('utf-8')
    return b2

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
    return render_template(
        'asset_portfolio.html',
        title='Asset',
        sunalt=plot()
    )
