from flask_login import login_required, current_user
from flask import render_template
from flask import Blueprint
import io
from base64 import b64encode
from flask import Blueprint, render_template
from flask import current_app as app
import matplotlib.pyplot as plt
from quantAPP.ext.profit.profit import stock
from quantAPP.ext.db.models import User


print(current_user)
for x in User.query.first().wallets.all():
    print(x.ticket)
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


@dashboard_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template(
        'dashboard/dashboard.html',
        title="Dashboard",
        sunalt=plot(),
    )




