from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from pandas_datareader import data as wb
from quantAPP.config import Config
import pandas as pd

config = Config()
engine = config.SQLALCHEMY_DATABASE_URI

class Stock:
    def __init__(self, ticket, name):
        self.ticket = ticket
        self.name = name

    def get_tables(self):
        if(self.ticket[-1].isdigit()):
            last_price = wb.get_data_yahoo(self.ticket + ".SA")
        else:
            last_price = wb.get_data_yahoo(self.ticket)
        return last_price

    def save(self):
        self.get_tables().to_sql(
            f"{self.name}", con=engine, if_exists="replace")
        return True


class Profit():
    def __init__(self, ticket):
        self.df = pd.read_sql_query(f"SELECT  * FROM {ticket}", engine)
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def calc_earnings(self,  last_value, first_value):
        earnings = round(float(last_value/first_value - 1) * 100, 2)
        return earnings

    def day(self):
        return float(self.df.tail(1)['Close'])

    def daily(self):
        last_day_df = self.df.tail(2).iloc[0]
        return self.calc_earnings(self.day(), last_day_df['Close'])

    def weekly(self):
        last_friday = datetime.today() - timedelta(days=date.today().weekday()+1)
        last_friday_df = self.df[self.df['Date'] < last_friday].tail(1)
        return self.calc_earnings(self.day(), last_friday_df['Close'])

    def monthly(self):
        last_month = datetime.today() - timedelta(days=date.today().day)
        last_month_df = self.df[self.df['Date'] <= last_month].tail(1)
        return self.calc_earnings(self.day(), last_month_df['Close'])

    def twelve_months(self):
        last_twelve_months = datetime.today() - relativedelta(years=1, days=1)
        last_twelve_months_df = self.df[self.df['Date']
                                        < last_twelve_months].tail(1)
        return self.calc_earnings(self.day(), last_twelve_months_df['Close'])

    def annual(self):
        last_year = datetime.today() - relativedelta(day=1, month=1, days=1)
        last_year_df = self.df[self.df['Date'] < last_year].tail(1)
        return self.calc_earnings(self.day(), last_year_df['Close'])

    def price(self):
        return {'day': f"{round(self.day(), 2):,}",
                'daily': self.daily(),
                'weekley': self.weekly(),
                'monthly': self.monthly(),
                'twelve_months': self.twelve_months(),
                'annual': self.annual()
                }


if __name__ == "__main__":
    ibov = Stock("^BVSP", 'ibovespa')
    dolar = Stock("BRL=X", 'dolar')
    sp500 = Stock("^GSPC", 'sp500')
    ifix = Stock('IFIX.SA', 'ifix')
    petr = Stock("petr4", 'petrobras_pn')
    # print(ibov.save())
    print(dolar.save())
    # print(sp500.save())
    # print(ifix.save())
    # print(petr.save())


    
    ibov = Profit('ibovespa')
    sp500 = Profit('sp500')
    dol = Profit('dolar')

    print(ibov.price())
    print(sp500.price())
    print(dol.price())
