from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from pandas_datareader import data as wb
from quantAPP.config import Config
from sqlalchemy import create_engine
import pandas as pd


config = Config()
path = r"C:\Users\wwwes\Documents\wwweslei-quantApp\quantAPP\ext\profit\company_files"
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=config.SQLALCHEMY_ECHO)


class Wallet:
    asset = pd.read_sql_query(
        "SELECT * FROM asset_portfolio", engine)

    @staticmethod
    def fii():
        fii = Wallet.asset[Wallet.asset['name'].str.startswith("FII")]
        return fii

    @staticmethod
    def bdr():
        bdr = Wallet.asset[Wallet.asset['ticket'].str.endswith('34')]
        return bdr

    @staticmethod
    def etf():
        all_end11 = Wallet.asset[Wallet.asset['ticket'].str.endswith('11')]
        fii = Wallet.asset[Wallet.asset['name'].str.startswith("FII")]
        etf = all_end11[all_end11.ticket.isin(fii['ticket']) == False]
        return etf

    @staticmethod
    def stocks():
        etf = Wallet.etf()
        bdr = Wallet.bdr()
        fii = Wallet.fii()
        etf_bdr_fii = pd.concat([etf, bdr, fii], ignore_index=bool)
        return Wallet.asset[Wallet.asset.ticket.isin(etf_bdr_fii['ticket']) == False]


def get_name_company(ticket):
    ticket.upper()
    stmt = f"""SELECT company FROM companies
                 where ticket1 = '{ticket}' or 
                       ticket2 = '{ticket}' or 
                       ticket3 = '{ticket}' or 
                       ticket4 = '{ticket}' or 
                       ticket5 = '{ticket}' or 
                       ticket6 = '{ticket}';"""
    return engine.execute(stmt).fetchone()[0]


def get_tickets_company(ticket):
    stmt = f"""SELECT "ticket1", "ticket2", "ticket3", "ticket4", "ticket5", "ticket6"
               FROM companies where company = '{get_name_company(ticket.upper())}';"""
    tickets = engine.execute(stmt).fetchone()
    tickets = set([x.replace('F', '') for x in tickets if(x)])
    return list(tickets)


def save(ticket, is_all=False):
    if(not is_all and ticket[-1].isdigit()):
        try:
            last_price = wb.get_data_yahoo(ticket + ".SA")
            last_price.to_sql(ticket, con=engine, if_exists="replace")
        except:
            return False
        return True
    if(ticket[-1].isdigit()):
        for ticket in get_tickets_company():
            last_price = wb.get_data_yahoo(ticket + ".SA")
            last_price.to_sql(ticket, con=engine, if_exists="replace")
    else:
        last_price = wb.get_data_yahoo(ticket)
        ticket.replace("^", "")
        last_price.to_sql(f"{ticket}", con=engine, if_exists="replace")
    return True


def update_value_companies():
    stmt = f"""SELECT "ticket1", "ticket2", "ticket3", "ticket4", "ticket5",
                     "ticket6" FROM companies"""
    companies = engine.execute(stmt).fetchall()
    full_tickets = []
    for tickets in companies:
        for ticket in tickets:
            full_tickets.append(ticket)
    full_tickets = sorted(
        list(set([x.replace('F', '') for x in full_tickets if(x)])))
    for ticket in full_tickets:
        try:
            print(save(ticket), "save -> ", ticket)
        except:
            print(save(ticket), "erro -> ", ticket)
            continue
    return "complete"


def update_value_fii():
    stmt = "SELECT Ticket FROM fii;"
    fiis = engine.execute(stmt).fetchall()
    for fii in fiis:
        fii = str(fii[0])
        try:
            print(save(fii), "save -> ", fii)
        except:
            print(save(fii), "ERRO -> ", fii)
            pass

    return "complete"


def calc_earnings(last_value, first_value):
    try:
        earnings = round(float(last_value/first_value - 1) * 100, 2)
    except:
        return 9999
    return earnings


def earnings(ticket):
    ticket = ticket.upper()
    df = pd.read_sql_query(f"SELECT  * FROM `{ticket}`", engine)
    df['Date'] = pd.to_datetime(df['Date'])
    day = float(df.tail(1)['Close'])
    daily = calc_earnings(day, df.tail(2).iloc[0]['Close'])
    last_friday = datetime.today() - timedelta(days=date.today().weekday()+1)
    last_friday_df = df[df['Date'] < last_friday].tail(1)
    weekly = calc_earnings(day, last_friday_df['Close'])
    last_month = datetime.today() - timedelta(days=date.today().day)
    last_month_df = df[df['Date'] <= last_month].tail(1)
    monthly = calc_earnings(day, last_month_df['Close'])
    last_twelve_months = datetime.today() - relativedelta(years=1, days=1)
    last_twelve_months_df = df[df['Date'] < last_twelve_months].tail(1)
    twelve_months = calc_earnings(day, last_twelve_months_df['Close'])
    last_year = datetime.today() - relativedelta(day=1, month=1, days=1)
    last_year_df = df[df['Date'] < last_year].tail(1)
    annual = calc_earnings(day, last_year_df['Close'])

    return {'day': f"{round(day, 2):,}",
            'daily': daily,
            'weekley': weekly,
            'monthly': monthly,
            'twelve_months': twelve_months,
            'annual': annual
            }


def ifix():
    df = wb.get_data_yahoo('ifix.sa')

    return {'day': f"{round(float(df['Close']) ,2):,}",
            'daily': calc_earnings(df['Close'], df['Open'])
            }

if __name__ == "__main__":
    carteira = Wallet.stocks()
    # print(carteira)
    carteira.plot.bar(x='name', y='qtde', rot=0)

