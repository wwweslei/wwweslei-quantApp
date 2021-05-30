from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
import pandas as pd


class InvestorParticipation:
    def __init__(self):
        self.engine = create_engine("sqlite:///banco.db", echo=True)
        self.URL = "https://sistemaswebb3-listados.b3.com.br/investorParticipationPage/"
        self.firefox = webdriver.Firefox()
        self.firefox.get(self.URL)

    def get_table(self):
        table = (
            WebDriverWait(self.firefox, 10)
            .until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            .get_attribute("outerHTML")
        )
        self.firefox.quit()
        df = pd.read_html(table)[0]
        df.columns = [
            "Tipo de Investidores",
            "Compras valor",
            "Compras part",
            "Vendas valor",
            "Vendas part",
        ]
        return df

    def save(self):
        df = self.get_table()
        df.to_sql(
            "investorParticipation", con=self.engine, if_exists="replace", index=False
        )


if __name__ == "__main__":
    participation = InvestorParticipation()
    participation.save()
