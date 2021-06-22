from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime


class Profit():
    def __init__(self, stock):
        self.engine = create_engine("sqlite:///banco.db", echo=False)
        self.stock = stock

    def calc_earnings(self, first_value, last_value):
        return round((first_value / last_value - 1) * 100, 2)

    def day(self):
        return float(pd.read_sql_query(f"SELECT  * FROM {self.stock}_DAILY", self.engine). tail(1)['Close'])

    def daily(self):
        yesterday = pd.read_sql_query(f"SELECT  * FROM {self.stock}_DAILY", self.engine).tail(2).iloc[0]['Close']
        return self.calc_earnings(self.day(), yesterday)

    def weekly(self):
        opening_weekly = pd.read_sql_query(f"SELECT  * FROM {self.stock}_weekly", self.engine).tail(2)['Open'].iloc[0]
        return self.calc_earnings(self.day(), opening_weekly)

    def monthly(self):
        opening_month = pd.read_sql_query(f"SELECT  * FROM {self.stock}_monthly", self.engine).tail(2)['Open'].iloc[0]
        return self.calc_earnings(self.day(), opening_month)

    def twelve_months(self):
        opening_twelve_months = pd.read_sql_query(f"SELECT  * FROM {self.stock}_monthly", self.engine).tail(13)['Open'].iloc[0]
        return self.calc_earnings(self.day(), opening_twelve_months)

    def annual(self):
        first_day_year = datetime(datetime.today().year, 1, 1)
        opening_annual = pd.read_sql_query(f"SELECT  * FROM {self.stock}_monthly", self.engine).tail(13)
        opening_annual['Date'] = pd.to_datetime(opening_annual['Date'])
        first_day_year = opening_annual[opening_annual['Date'] >= first_day_year].iloc[0]['Open']
        return self.calc_earnings(self.day(), first_day_year)
  

if __name__ == "__main__":
    profit = Profit('ibovespa')
    print('daily', profit.daily())
    print('weekley', profit.weekly())
    print('monthly', profit.monthly())
    print('twelve_months', profit.twelve_months())
    print('twelve_annual', profit.annual())
