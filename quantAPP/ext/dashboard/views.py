from flask_login import login_required
from flask import render_template
from flask import render_template
from flask_login import login_required
from flask import Blueprint
import io
from base64 import b64encode
from flask import Blueprint, render_template
from flask import current_app as app
import yfinance as yf
import matplotlib.pyplot as plt


dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)


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


@dashboard_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template(
        'dashboard/dashboard.html',
        title="Dashboard",
        sunalt=plot()
    )




