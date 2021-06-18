from quantAPP.config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
import pandas as pd


class Crawler_cei:
    def __init__(self):
        config = Config()
        self.cpf = config.CPF
        self.key = config.KEY
        self.URL = "https://ceiapp.b3.com.br/CEI_Responsivo/"
        self.engine = create_engine("sqlite:///banco.db", echo=True)
        self.firefox = webdriver.Firefox()
        self.asset_table_id_0 = "ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl01_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"
        self.asset_table_id_1 = "ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl01_rptContaMercado_ctl00_rprCarteira_ctl01_grdCarteira"
        self.treasury_direct_id = "ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl01_rptContaMercado_ctl00_trBodyTesouroDireto"

    def login(self):
        self.firefox.get(self.URL)
        input_login = self.firefox.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtLogin"]')
        input_login.send_keys(self.cpf)
        input_key = self.firefox.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtSenha"]')
        input_key.send_keys(self.key)
        btn_login = self.firefox.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnLogar"]')
        btn_login.click()
        try:
            WebDriverWait(self.firefox, 60).until(EC.visibility_of_element_located((By.ID, "objGrafPosiInv")))
        except Exception:
            raise Exception("It was not possible to log into the CEI.")

    def __navigate_to_asset_portfolio(self):
        self.firefox.get(self.URL + "ConsultarCarteiraAtivos.aspx")
        WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_btnConsultar"))).click()
        WebDriverWait(self.firefox, 30).until(EC.visibility_of_element_located((By.ID, self.asset_table_id_0)))

    def get_asset_portfolio(self):
        self.__navigate_to_asset_portfolio()
        table_free_wallet = self.firefox.find_element_by_id(self.asset_table_id_0).get_attribute("outerHTML")
        df_free_wallet = pd.read_html(table_free_wallet, decimal=",", thousands=".")[0][0:-1]
        table_derivative_guarantee = self.firefox.find_element_by_id(self.asset_table_id_1).get_attribute("outerHTML")
        df_derivative_guarantee = pd.read_html(table_derivative_guarantee, decimal=",", thousands=".")[0][0:-1]
        df= pd.merge(df_free_wallet, df_derivative_guarantee, how="outer")
        df.columns = [
            "empresa",
            "tipo",
            "cod",
            "codISIN",
            "Valor",
            "qtde",
            "fator",
            "total",
        ]
        return df

    def get_treasury_direct(self):
        self.__navigate_to_asset_portfolio()
        table_treasury = self.firefox.find_element_by_id(self.treasury_direct_id).get_attribute("outerHTML")
        df_treasury = pd.read_html(table_treasury, decimal=",", thousands=".")[0]
        df_treasury.columns = [
            "título",
            "vencimento",
            "investido",
            "bruto",
            "liquido",
            "total",
            "bloqueado",
        ]
        return df_treasury[0:-1]

    def save(self):
        self.login()
        df_asset_portfolio = self.get_asset_portfolio()
        df_asset_portfolio.to_sql("asset_portfolio", con=self.engine, if_exists="replace", index=False)
        df_treasury_direct = self.get_treasury_direct()
        df_treasury_direct.to_sql("treasury_direct", con=self.engine, if_exists="replace", index=False)
        self.firefox.quit()


if __name__ == "__main__":
    cei = Crawler_cei()
    cei.save()
