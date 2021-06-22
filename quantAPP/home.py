from flask import Blueprint, render_template
from flask import current_app as app
from quantAPP.ext.index import Index
import pandas as pd
from . import db


ibov = Index()
# ibov.save()
sp500 = Index("^GSPC")
# sp500.save()




home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/<update>', methods=['GET'])
@home_bp.route('/', methods=['GET'])
def home(update=False):
    if(update == "ibov_update"):
        ibov = Index()
        ibov.save()
        pass
    if(update == "sp500_update"):
        sp500 = Index("^GSPC")
        sp500.save()
        pass
    if(update == "dol_update"):
        dol = Index("BRL=X")
        dol.save()
        pass
    ibov = pd.read_sql_query(
        "SELECT  * FROM ibov", db.get_engine())
    sp500 = pd.read_sql_query(
        "SELECT  * FROM sp500", db.get_engine())
    dol = pd.read_sql_query(
        "SELECT  * FROM cambio_daily", db.get_engine())
    return render_template(
        'index.html',
        title='Dashboard',
        ibov=ibov,
        sp500 = sp500,
        dol= round(float(dol.tail(1)["Close"]), 4)
    )
