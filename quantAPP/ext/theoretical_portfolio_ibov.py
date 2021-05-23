from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine

import pandas as pd
from time import sleep


class Theoretical_portfolio_ibov():
    def __init__(self):
        self.TIME_TO_LOAD_THE_TABLE_INTO_THE_DOM = 9
        self.URL = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
        self.engine = create_engine("sqlite:///banco.db", echo=True)
        self.firefox = webdriver.Firefox()
        self.firefox.get(self.URL)

    def get_portfolio_ibov(self):
        for _cont_number_repeat in range(3):
            WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.ID, "selectPage"))).send_keys(Keys.ARROW_DOWN)
        sleep(self.TIME_TO_LOAD_THE_TABLE_INTO_THE_DOM)
        table = self.firefox.find_element_by_class_name('table').get_attribute("outerHTML")
        self.firefox.quit()
        df = pd.read_html(table)[0]
        df.drop(df.tail(2).index, inplace=True)
        return df

    def save(self):
        df = self.get_portfolio_ibov()
        df.to_sql("Index_ibov", con=self.engine, if_exists="replace", index=False)
        


if __name__ == "__main__":
    ibov = Theoretical_portfolio_ibov()
    ibov.save()