from pandas_datareader import data as wb
import pandas as pd
import pprint
from sqlalchemy import create_engine

class Stock:
    def __init__(self, ticket, name):
        self.ticket = ticket
        self.name = name
        self.engine = create_engine("sqlite:///banco.db", echo=True)

    def get_historical_data(self, frequency):
        if(self.ticket[-1].isdigit()):
            last_price = wb.get_data_yahoo(self.ticket + ".SA", interval=frequency)
        else:
            last_price = wb.get_data_yahoo(self.ticket, interval=frequency)
        return last_price

    def get_tables(self):
        return [self.get_historical_data(frequency) for frequency in ["d", "w", "m"]]


    def save(self):
        tables = self.get_tables()
        for table, frequency in zip(tables, ["daily", "weekly", "monthly"]):
            table.to_sql(f"{self.name}_{frequency}", con=self.engine, if_exists="replace")
        return True



if __name__ == '__main__':
    index = Stock("^BVSP", 'ibovespa')
    index = Stock("BRL=X", 'cambio')
    print(index.save())
