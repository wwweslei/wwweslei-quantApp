from flask import Blueprint, render_template
from flask import current_app as app
import pandas as pd
from quantAPP.ext.profit import profit

fii = profit.Wallet.fii()
stocks = profit.Wallet.stocks()
bdr = profit.Wallet.bdr()
etf = profit.Wallet.etf()

wallet = {
    'FII': fii['total'].astype(float).sum(),
    'BDR': bdr['total'].astype(float).sum(),
    'ETF': etf['total'].astype(float).sum(),
    'AÇÕES': stocks['total'].astype(float).sum(),
}

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


def create_dictionary(df):
    df = df.groupby(pd.Grouper(freq='M')).last()[-13:]['Close']
    data = {month: float(close/df.head(1)-1)
            for (month, close) in zip(df.index.strftime('%m/%y'), df)}
    return data


@home_bp.route('/<update>', methods=['GET'])
@home_bp.route('/', methods=['GET'])
def home(update=False):
    if(update == "ibov_update"):
        profit.ind(is_update=True)
        pass
    if(update == "sp500_update"):
        profit.sp500(is_update=True)
        pass
    if(update == "dol_update"):
        profit.wdo(is_update=True)
        pass
    if(update == "ifix_update"):
        profit.ifix(is_update=True)
        pass

    return render_template(
        'index.html',
        title='Dashboard',
        ibov=profit.earnings("IND"),
        sp500=profit.earnings("SP500"),
        dol=profit.earnings("WDO"),
        ifix=profit.earnings("IFIX"),
        stocks=stocks[['name', 'total']],
        fii=fii[['name', 'total']],
        bdr=bdr[['name', 'total']],
        etf=etf[['name', 'total']],
        wallet=wallet,
        ind=create_dictionary(profit.ind()),
        sp=create_dictionary(profit.sp500()),
        wdo=create_dictionary(profit.wdo()),
        ifix0=create_dictionary(profit.ifix()),
    )
