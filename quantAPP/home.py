from flask import Blueprint, render_template
from flask import current_app as app
from quantAPP.ext.profit import profit 


home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/<update>', methods=['GET'])
@home_bp.route('/', methods=['GET'])
def home(update=False):
    if(update == "ibov_update"):
        profit.save("^BVSP")
        pass
    if(update == "sp500_update"):
        profit.save("^GSPC")
        pass
    if(update == "dol_update"):
        profit.save("BRL=X")
        pass
    if(update == "ifix_update"):
        profit.ifix()
        pass

    return render_template(
        'index.html',
        title='Dashboard',
        ibov=profit.earnings("BVSP"),
        sp500=profit.earnings("GSPC"),
        dol=profit.earnings("BRL=X"),
        ifix=profit.ifix(),
    )
