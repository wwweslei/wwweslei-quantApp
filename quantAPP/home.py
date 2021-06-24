from flask import Blueprint, render_template
from flask import current_app as app
from quantAPP.ext.profit import Profit, Stock


ibov = Stock("^BVSP", 'ibovespa')
# ibov.save()
sp500 = Stock("^GSPC", 'sp500')
# sp500.save()
dol = Stock("BRL=X", 'dolar')
# dol.save()


home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/<update>', methods=['GET'])
@home_bp.route('/', methods=['GET'])
def home(update=False):
    if(update == "ibov_update"):
        ibov = Stock("^BVSP", 'ibovespa')
        ibov.save()
        pass
    if(update == "sp500_update"):
        sp500 = Stock("^GSPC", 'sp500')
        sp500.save()
        pass
    if(update == "dol_update"):
        dol = Stock("BRL=X", 'dolar')
        dol.save()
        pass
    ibov = Profit('ibovespa')
    dol = Profit('dolar')
    sp500 = Profit('sp500')

    return render_template(
        'index.html',
        title='Dashboard',
        ibov=ibov.price(),
        sp500 = sp500.price(),
        dol= dol.price(),
    )
