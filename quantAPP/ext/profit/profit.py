from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from pandas_datareader import data as wb
from quantAPP.config import Config
from sqlalchemy import create_engine
import pandas as pd


config = Config()
engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       echo=config.SQLALCHEMY_ECHO)


def listed_companies_by_sector_update():
    df = pd.read_html("https://www.infomoney.com.br/cotacoes/empresas-b3/")
    frames = [
        df[10].assign(Setor="Utilidade Pública"),
        df[9].assign(Setor="Telecomunicações"),
        df[8].assign(Setor="Tecnologia da Informação"),
        df[7].assign(Setor="Saúde"),
        df[6].assign(Setor="Petróleo, Gás e Biocombustíveis"),
        df[4].assign(Setor="Materiais Básicos"),
        df[5].assign(Setor="Outros"),
        df[3].assign(Setor="Financeiro"),
        df[2].assign(Setor="Consumo não Cíclico"),
        df[1].assign(Setor="Consumo Cíclico"),
        df[0].assign(Setor="Bens Industriais"),
    ]
    result = pd.concat(frames, ignore_index=True)
    result['Empresas'] = result['Empresas'].str.upper()
    result.columns = ["company", "ticket1", "ticket2", "ticket3", "ticket4", "ticket5", "ticket6", "setor"]
    result.to_sql("listed_companies_by_sector", con=engine,
                  if_exists="replace", index=False)
    return True


def get_name(ticket):
    ticket.upper()
    stmt = f"""SELECT company FROM listed_companies_by_sector
                 where ticket1 = '{ticket}' or 
                       ticket2 = '{ticket}' or 
                       ticket3 = '{ticket}' or 
                       ticket4 = '{ticket}' or 
                       ticket5 = '{ticket}' or 
                       ticket6 = '{ticket}';"""
    return engine.execute(stmt).fetchone()[0]


def get_tickets(ticket):
    stmt = f"""SELECT "ticket1", "ticket2", "ticket3", "ticket4", "ticket5", "ticket6"
                    FROM listed_companies_by_sector
                    where company = '{get_name(ticket.upper())}';"""
    tickets = engine.execute(stmt).fetchone()
    tickets = set([x.replace('F', '') for x in tickets if(x)])
    return list(tickets)


def save(ticket, is_all=False):
    if(not is_all and ticket[-1].isdigit()):
        last_price = wb.get_data_yahoo(ticket + ".SA")
        last_price.to_sql(ticket, con=engine, if_exists="replace")
        return True
    if(ticket[-1].isdigit()):
        for ticket in get_tickets():
            last_price = wb.get_data_yahoo(ticket + ".SA")
            last_price.to_sql(ticket, con=engine, if_exists="replace")
    else:
        last_price = wb.get_data_yahoo(ticket)
        ticket.replace("^", "")
        last_price.to_sql(f"{ticket}", con=engine, if_exists="replace")
    return True


def update():
    stmt = stmt = f"""SELECT "ticket1", "ticket2", "ticket3", "ticket4", "ticket5", "ticket6"
                    FROM listed_companies_by_sector
                    """
    companies = engine.execute(stmt).fetchall()
    full_tickets = []
    for tickets in companies:
        for ticket in tickets:
            full_tickets.append(ticket)
    full_tickets = sorted(
        list(set([x.replace('F', '') for x in full_tickets if(x)])))
    for ticket in full_tickets:
        try:
            print(save(ticket), ticket)
        except:
            continue


def calc_earnings(last_value, first_value):
    earnings = round(float(last_value/first_value - 1) * 100, 2)
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
    print(ifix())
