from flask import Blueprint, render_template
from flask import current_app as app
import pandas as pd
from quantAPP.ext.profit import profit


home_blueprint = Blueprint("home", __name__)


def create_dictionary(df):
    df = df.groupby(pd.Grouper(freq="M")).last()[-13:]["Close"]
    data = {
        month: float(close / df.head(1) - 1)
        for (month, close) in zip(df.index.strftime("%m/%y"), df)
    }
    return data


@home_blueprint.route("/<update>", methods=["GET"])
@home_blueprint.route("/")
def homepage(update=False):
    if update == "ibov_update":
        profit.ind(is_update=True)
        pass
    if update == "sp500_update":
        profit.sp500(is_update=True)
        pass
    if update == "dol_update":
        profit.wdo(is_update=True)
        pass
    if update == "ifix_update":
        profit.ifix(is_update=True)
        pass

    return render_template(
        "home/index.html",
        title="Dashboard",
        ibov=profit.earnings(profit.ind()),
        sp500=profit.earnings(profit.sp500()),
        dol=profit.earnings(profit.wdo()),
        ifix=profit.earnings(profit.ifix()),
        ind=create_dictionary(profit.ind()),
        sp=create_dictionary(profit.sp500()),
        wdo=create_dictionary(profit.wdo()),
        ifix0=create_dictionary(profit.ifix()),
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("home/404.html"), 404
