from datetime import date
from quantAPP.config import Config
from sqlalchemy import create_engine
import pandas_datareader.data as web
from typing import Dict
import yfinance as yf
import pandas as pd


config = Config()
path = r"C:\Users\wwwes\Documents\wwweslei-quantApp\quantAPP\ext\profit\company_files"
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=config.SQLALCHEMY_ECHO)


# class Wallet:
#     asset = pd.read_sql_query("SELECT * FROM asset_portfolio", con=engine)

#     @staticmethod
#     def fii() -> pd.DataFrame:
#         fii = Wallet.asset[Wallet.asset["name"].str.startswith("FII")]
#         return fii

#     @staticmethod
#     def bdr() -> pd.DataFrame:
#         bdr = Wallet.asset[Wallet.asset["ticket"].str.endswith("34")]
#         return bdr

#     @staticmethod
#     def etf() -> pd.DataFrame:
#         all_end11 = Wallet.asset[Wallet.asset["ticket"].str.endswith("11")]
#         fii = Wallet.asset[Wallet.asset["name"].str.startswith("FII")]
#         etf = all_end11[all_end11.ticket.isin(fii["ticket"]) == False]
#         return etf

#     @staticmethod
#     def stocks() -> pd.DataFrame:
#         etf = Wallet.etf()
#         bdr = Wallet.bdr()
#         fii = Wallet.fii()
#         etf_bdr_fii = pd.concat([etf, bdr, fii], ignore_index=bool)
#         return Wallet.asset[Wallet.asset.ticket.isin(etf_bdr_fii["ticket"]) == False]


def calc(last_value: float, first_value: float) -> float:
    return round(float(last_value / first_value - 1) * 100, 2)


def earnings(df: pd.DataFrame) -> Dict[str, int]:
    day = float(df.tail(1)["Close"])
    return {
        "day": f"{round(day, 2):,}",
        "daily": calc(day, df.tail(2).iloc[0]["Close"]),
        "weekly": calc(day, df.groupby(pd.Grouper(freq="w")).last()[-2:-1]["Close"]),
        "monthly": calc(day, df.groupby(pd.Grouper(freq="M")).last()[-2:-1]["Close"]),
        "twelve_months": calc(
            day, df.groupby(pd.Grouper(freq="M")).last()[-13:-12]["Close"]
        ),
        "annual": calc(
            day,
            df.groupby(pd.Grouper(freq="M"))
            .last()[-(date.today().month + 1) :]["Close"]
            .head(1),
        ),
    }


def stock(ticket: str, is_update: bool = False) -> pd.DataFrame:
    ticket = ticket.upper()
    if is_update:
        df = yf.download(ticket + ".SA")
        df.to_sql(ticket.removesuffix(".SA"), con=engine, if_exists="replace")
        return df
    try:
        df = pd.read_sql(f"SELECT * FROM {ticket}", con=engine, index_col="Date")
        df.index = pd.to_datetime(df.index)
        return df
    except:
        df = stock(ticket, is_update=True)
        return df


def ind(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = yf.download("^BVSP")
        df.to_sql("IND", con=engine, if_exists="replace")
        return df
    try:
        df = pd.read_sql("SELECT * FROM IND", con=engine, index_col="Date")
        df.index = pd.to_datetime(df.index)
        return df
    except:
        df = ind(is_update=True)
        return df


def sp500(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = yf.download("^GSPC")
        df.to_sql("SP500", con=engine, if_exists="replace")
        return df
    try:
        df = pd.read_sql(
            "SELECT * FROM SP500",
            con=engine,
            index_col="Date",
        )
        df.index = pd.to_datetime(df.index)
        return df
    except:
        df = sp500(is_update=True)
        return df


def ifix(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = web.get_data_alphavantage("ifix.sa", api_key=config.API_KEY)
        df.index = pd.to_datetime(df.index)
        df.columns = ["Open", "High", "Low", "Close", "Volume"]
        df.index.names = ["Date"]
        df.to_sql("IFIX", con=engine, if_exists="replace")
        return df
    try:
        df = pd.read_sql("SELECT * FROM IFIX", con=engine, index_col="Date")
        df.index = pd.to_datetime(df.index)
        return df
    except:
        df = ifix(is_update=True)
        return df


def wdo(is_update: bool = False) -> pd.DataFrame:
    if is_update:
        df = web.DataReader("usd/brl", "av-forex-daily", api_key=config.API_KEY)
        df.index = pd.to_datetime(df.index)
        df.columns = ["Open", "High", "Low", "Close"]
        df.index.names = ["Date"]
        df.to_sql("WDO", con=engine, if_exists="replace")
        return df
    try:
        df = pd.read_sql("SELECT * FROM WDO", con=engine, index_col="Date")
        df.index = pd.to_datetime(df.index)
        return df
    except:
        df = wdo(is_update=True)
        return df


def info(ticket: str, is_update: bool = False) -> pd.DataFrame:
    ticket = ticket.lower()
    if is_update:
        df = yf.Ticker(ticket + ".sa").info
        df = pd.DataFrame.from_dict(df, orient="index", columns=["Value"])
        df = df.loc[
            [
                "sector",
                "shortName",
                "longName",
                "logo_url",
                "symbol",
                "ebitda",
                "targetLowPrice",
                "recommendationKey",
                "targetMedianPrice",
                "currentPrice",
                "earningsGrowth",
                "totalCash",
                "totalDebt",
                "totalRevenue",
                "recommendationMean",
                "exchange",
                "yield",
                "beta",
                "ytdReturn",
                "category",
                "previousClose",
                "open",
                "dividendRate",
                "exDividendDate",
                "marketCap",
                "volume",
                "dividendYield",
                "bidSize",
                "dayHigh",
            ]
        ]
        df.T.to_sql(ticket + "_info", con=engine, if_exists="replace")
        return df.T
    try:
        return pd.read_sql(f"SELECT * FROM {ticket}_info", con=engine)
    except:
        df = info(ticket, is_update=True)
        return df.T


if __name__ == "__main__":
    d = info("rect11")
    print(d.sector.values)
