from time import sleep
from selenium.webdriver.common.keys import Keys
from quantAPP.config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
from quantAPP.config import Config
import pandas as pd



config = Config()
options = Options()
path = r"C:\Users\wwwes\Documents\wwweslei-quantApp\quantAPP\ext\profit\company_files"
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=config.SQLALCHEMY_ECHO)
preferences = {"download.default_directory": path,
               "directory_upgrade": True,
               "safebrowsing.enabled": True
               }
options.add_experimental_option("prefs", preferences)
options.headless = False


class Crawler_cei:
    def __init__(self):
        config = Config()
        self.cpf = config.CPF
        self.key = config.KEY
        self.URL = "https://ceiapp.b3.com.br/CEI_Responsivo/"
        self.firefox = webdriver.Chrome(options=options)
        self.asset_table_id_0 = "ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl01_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"
        self.asset_table_id_1 = "ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl01_rptContaMercado_ctl00_rprCarteira_ctl01_grdCarteira"
        self.treasury_direct_id = "ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl01_rptContaMercado_ctl00_trBodyTesouroDireto"

    def __login(self):
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
            "name",
            "tipo",
            "ticket",
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
        self.__login()
        df_asset_portfolio = self.get_asset_portfolio()
        df_asset_portfolio.to_sql("asset_portfolio", con=engine, if_exists="replace", index=False)
        df_treasury_direct = self.get_treasury_direct()
        df_treasury_direct.to_sql("treasury_direct", con=engine, if_exists="replace", index=False)
        self.firefox.quit()
        return True


class CrawlerCvmCod:
    def __init__(self):
        self.URL = "https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/ResultBuscaParticCiaAb.aspx?CNPJNome=&TipoConsult=C"

    def get_table(self):
        df = pd.read_html(self.URL)[0]
        df.columns = ["CNPJ", "NOME", "TIPO", "CÓDIGO", "SITUAÇÃO"]
        df.drop(df.head(1).index, inplace=True)
        return df[df.SITUAÇÃO.str.startswith("Concedido")]

    def save(self):
        self.get_table().to_sql("code_cvm", con=engine, if_exists="replace", index=False)
        return True


class Crawler_theoretical_portfolio_ibov:
    def __init__(self):
        self.TIME_TO_LOAD_THE_TABLE_INTO_THE_DOM = 2
        self.URL = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
        self.engine = engine
        self.firefox = webdriver.Firefox()
        self.firefox.get(self.URL)

    def get_table(self):
        for _cont_number_repeat in range(3):
            WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located(
                (By.ID, "selectPage"))).send_keys(Keys.ARROW_DOWN)
        sleep(self.TIME_TO_LOAD_THE_TABLE_INTO_THE_DOM)
        table = self.firefox.find_element_by_class_name(
            "table").get_attribute("outerHTML")
        self.firefox.quit()
        df = pd.read_html(table)[0]
        df.drop(df.tail(2).index, inplace=True)
        return df

    def save(self):
        df = self.get_table()
        df.to_sql("Index_ibov", con=self.engine,
                  if_exists="replace", index=False)


class Crawler_ibov_index_companies:
    def __init__(self):
        self.engine = engine
        self.__URL = "http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?idioma=pt-br"
        self.ID_BUTTON = "ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_btnTodas"
        self.ID_TABLE = "ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01"
        self.firefox = webdriver.Firefox()
        self.firefox.get(self.__URL)

    def get_table(self):
        WebDriverWait(self.firefox, 10).until(
            EC.presence_of_element_located((By.ID, self.ID_BUTTON))).click()

        table = WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located(
            (By.ID, self.ID_TABLE))).get_attribute("outerHTML")
        self.firefox.quit()
        return pd.read_html(table)[0]

    def save(self):
        df = self.get_table()
        df.to_sql("ibov_index_companies", con=self.engine,
                  if_exists="replace", index=False)


class Crawler_investorParticipation:
    def __init__(self):
        self.engine = engine
        self.URL = "https://sistemaswebb3-listados.b3.com.br/investorParticipationPage/"
        self.firefox = webdriver.Chrome()
        self.firefox.get(self.URL)

    def get_table(self):
        table = WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located(
            (By.TAG_NAME, "table"))).get_attribute("outerHTML")
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
        df.to_sql("investorParticipation", con=self.engine,
                  if_exists="replace", index=False)


class Crawler_csv_fii:
    @staticmethod
    def get_table():
        chrome = webdriver.Chrome(options=options)
        URL = "https://sistemaswebb3-listados.b3.com.br/fundsPage/7"
        chrome.get(URL)
        xpath = '//*[@id="divContainerIframeB3"]/div/div/div/div[1]/div[2]/p/a'
        sleep(2)
        chrome.find_element_by_xpath(xpath).click()
        sleep(3)
        return True

    @staticmethod
    def save():
        df = pd.read_csv(path + '\\fundosListados.csv', sep=';')
        df.columns = ["Name", "_", "Ticket", "__"]
        df["Ticket"] = df["Ticket"]+"11"
        df["Name"].replace({r"FII .[A-Z]..*", 'ddd'}, inplace=True, regex=True)
        df[["Name", "Ticket"]].to_sql("fii", con=engine, if_exists="replace")
        return True


def Crawler_tb_company():
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
    result.columns = ["company", "ticket1", "ticket2",
                      "ticket3", "ticket4", "ticket5", "ticket6", "setor"]
    result.to_sql("companies", con=engine, if_exists="replace", index=False)
    return True




if __name__ == "__main__":
    a = Crawler_cei()
    print(a.save())
