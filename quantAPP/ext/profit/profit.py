from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from quantAPP.config import Config
from sqlalchemy import create_engine
import pandas_datareader.data as web
from typing import Dict
import yfinance as yf
import pandas as pd


config = Config()
path = r"C:\Users\wwwes\Documents\wwweslei-quantApp\quantAPP\ext\profit\company_files"
engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       echo=config.SQLALCHEMY_ECHO)


class Wallet:
    asset = pd.read_sql_query("SELECT * FROM asset_portfolio", engine)

    @staticmethod
    def fii() -> pd.DataFrame:
        fii = Wallet.asset[Wallet.asset["name"].str.startswith("FII")]
        return fii

    @staticmethod
    def bdr() -> pd.DataFrame:
        bdr = Wallet.asset[Wallet.asset["ticket"].str.endswith("34")]
        return bdr

    @staticmethod
    def etf() -> pd.DataFrame:
        all_end11 = Wallet.asset[Wallet.asset["ticket"].str.endswith("11")]
        fii = Wallet.asset[Wallet.asset["name"].str.startswith("FII")]
        etf = all_end11[all_end11.ticket.isin(fii["ticket"]) == False]
        return etf

    @staticmethod
    def stocks() -> pd.DataFrame:
        etf = Wallet.etf()
        bdr = Wallet.bdr()
        fii = Wallet.fii()
        etf_bdr_fii = pd.concat([etf, bdr, fii], ignore_index=bool)
        return Wallet.asset[Wallet.asset.ticket.isin(etf_bdr_fii["ticket"]) == False]


def __calc_earnings(last_value: float, first_value: float) -> float:
    return round(float(last_value / first_value - 1) * 100, 2)


def earnings(ticket: str) -> Dict[str, int]:
    ticket = ticket.upper()
    df = pd.read_sql_query(f"SELECT  * FROM `{ticket}`", engine)
    df["Date"] = pd.to_datetime(df["Date"])
    day = float(df.tail(1)["Close"])
    daily = __calc_earnings(day, df.tail(2).iloc[0]["Close"])
    last_friday = datetime.today() - timedelta(days=date.today().weekday() + 1)
    last_friday_df = df[df["Date"] < last_friday].tail(1)
    weekly = __calc_earnings(day, last_friday_df["Close"])
    last_month = datetime.today() - timedelta(days=date.today().day)
    last_month_df = df[df["Date"] <= last_month].tail(1)
    monthly = __calc_earnings(day, last_month_df["Close"])
    last_twelve_months = datetime.today() - relativedelta(years=1, day=29) #review
    last_twelve_months_df = df[df["Date"] < last_twelve_months].tail(1)
    twelve_months = __calc_earnings(day, last_twelve_months_df["Close"])
    last_year = datetime.today() - relativedelta(day=1, month=1, days=1)
    last_year_df = df[df["Date"] < last_year].tail(1)
    annual = __calc_earnings(day, last_year_df["Close"])

    return {
        "day": f"{round(day, 2):,}",
        "daily": daily,
        "weekly": weekly,
        "monthly": monthly,
        "twelve_months": twelve_months,
        "annual": annual,
    }


def stock(ticket: str, is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = yf.download(ticket)
        df.to_sql(ticket, con=engine, if_exists="replace")
        return df
    df = pd.read_sql(f"SELECT * FROM {ticket}", con=engine, index_col="Date")
    df.index = pd.to_datetime(df.index)
    return df


def ind(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = yf.download("^BVSP")
        df.to_sql("IND", con=engine, if_exists="replace")
        return df
    df = pd.read_sql("SELECT * FROM IND", con=engine, index_col="Date")
    df.index = pd.to_datetime(df.index)
    return df


def sp500(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = yf.download("^GSPC")
        df.to_sql("SP500", con=engine, if_exists="replace")
        return df
    df = pd.read_sql("SELECT * FROM SP500", con=engine, index_col="Date")
    df.index = pd.to_datetime(df.index)
    return df


def ifix(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = web.get_data_alphavantage("ifix.sa", api_key=config.API_KEY)
        df.index = pd.to_datetime(df.index)
        df.columns = ["Open", "High", "Low", "Close", "Volume"]
        df.index.names = ["Date"]
        df.to_sql("IFIX", con=engine, if_exists="replace")
        return df
    df = pd.read_sql("SELECT * FROM IFIX", con=engine, index_col="Date")
    df.index = pd.to_datetime(df.index)
    return df


def wdo(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = web.DataReader("usd/brl", "av-forex-daily",
                            api_key=config.API_KEY)
        df.index = pd.to_datetime(df.index)
        df.columns = ["Open", "High", "Low", "Close"]
        df.index.names = ["Date"]
        df.to_sql("WDO", con=engine, if_exists="replace")
        return df
    df = pd.read_sql("SELECT * FROM WDO", con=engine, index_col="Date")
    df.index = pd.to_datetime(df.index)
    return df


def create_dictionary(df):
    df = df.groupby(pd.Grouper(freq='M')).last()[-13:]['Close']
    data = {month: float(close/df.head(1)-1)
            for (month, close) in zip(df.index.strftime('%m/%y'), df)}
    return data

if __name__ == "__main__":
    df = sp500()
