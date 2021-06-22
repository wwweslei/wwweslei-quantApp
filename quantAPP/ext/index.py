from datetime import date, timedelta
from pandas_datareader import data as wb
import pandas as pd
from sqlalchemy import create_engine


class Index:
    def __init__(self, index="^BVSP"):
        self.index = index
        self.engine = create_engine("sqlite:///banco.db", echo=True)
        self.parcer_index = {"^BVSP": "ibov", "^GSPC": "sp500"}

    def format_date(self, date):
        return date.strftime("%d/%m/%Y")

    def first_day_week(self):
        return self.format_date(date.today() - timedelta(days=date.today().isoweekday() - 1))

    def first_day_month(self):
        if (date.today() - timedelta(days=date.today().day - 1)).isoweekday() == 6:
            return date.today() - timedelta(days=date.today().day - 3)
        if (date.today() - timedelta(days=date.today().day - 1)).isoweekday() == 7:
            return date.today() - timedelta(days=date.today().day - 2)
        return self.format_date(date.today() - timedelta(days=date.today().day - 1))

    def first_day_year(self):
        return self.format_date(date(date.today().year, 1, 2))

    def get_last_price(self, ticket):
        if(ticket[-1].isdigit()):
            last_price = wb.get_data_yahoo(ticket + ".SA").tail(1).Close[0]
        else:
            last_price = wb.get_data_yahoo(ticket).tail(1).Close[0]
        return round(last_price, 2)

    def index_values(self):
        values = wb.get_data_yahoo(self.index)
        index = {
            "annual": float(values.loc[self.first_day_year()].Open),
            "monthly": float(values.loc[self.first_day_month()].Open),
            "weekly": float(values.loc[self.first_day_week()].Open),
            "daily": values.tail(1).iloc[0].Close,
            "last_day": values.tail(2).iloc[0].Close
        }
        return index

    def calc_earnings(self, first_value, last_value):
        return round((first_value / last_value - 1) * 100, 2)

    def get_table(self):
        index = self.index_values()
        index_earnings = {"last_day": f'{index["last_day"]:,.2f}'.replace(",", "."),
                          "day": [f'{index["daily"]:,.2f}'.replace(",", ".")],
                          "annual": f'{self.calc_earnings(index["daily"], index["annual"])}%',
                          "monthly": f'{self.calc_earnings(index["daily"], index["monthly"])}%',
                          "weekly": f'{self.calc_earnings(index["daily"], index["weekly"])}%',
                          "daily": f'{self.calc_earnings(index["daily"], index["last_day"])}%'
                          }
        return pd.DataFrame(index_earnings)

    def save(self):
        self.get_table().to_sql(self.parcer_index[self.index], con=self.engine,
                                if_exists="replace", index=False)


if __name__ == "__main__":
    index = Index("^BVSP")
    print(index.save())
