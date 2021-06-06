from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
import pandas as pd


class BuscaEmpresaListada:
    def __init__(self):
        self.engine = create_engine("sqlite:///banco.db", echo=True)
        self.__URL = "http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?idioma=pt-br"
        self.ID_BUTTON = "ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_btnTodas"
        self.ID_TABLE = "ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01"
        self.firefox = webdriver.Firefox()
        self.firefox.get(self.__URL)

    def get_table(self):
        WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.ID, self.ID_BUTTON))).click()

        table = WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.ID, self.ID_TABLE))).get_attribute("outerHTML")
        self.firefox.quit()
        return pd.read_html(table)[0]

    def save(self):
        df = self.get_table()
        df.to_sql("empresas", con=self.engine, if_exists="replace", index=False)


if __name__ == "__main__":
    empresaListada = BuscaEmpresaListada()
    empresaListada.save()
