import pandas as pd
import requests
from sqlalchemy import create_engine


class CodeCvm:
    def __init__(self):
        self.URL = "https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/ResultBuscaParticCiaAb.aspx?CNPJNome=&TipoConsult=C"
        self.engine = create_engine("sqlite:///banco.db", echo=True)

    def get_table(self):
        response = requests.get(self.URL).content
        df = pd.read_html(response)[0]
        df.columns = ["CNPJ", " NOME", "TIPO", "CÓDIGO", "SITUAÇÃO"]
        df.drop(df.head(1).index, inplace=True)
        return df[df.SITUAÇÃO.str.startswith("Concedido")]

    def save(self):
        df = self.get_table()
        df.to_sql("Code_cvm", con=self.engine, if_exists="replace", index=False)


if __name__ == "__main__":
    code = CodeCvm()
    code.save()
