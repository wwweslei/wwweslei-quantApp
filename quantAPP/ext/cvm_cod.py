import pandas as pd
from sqlalchemy import create_engine


class CodeCvm():
    def __init__(self):
        self.URL = "https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/ResultBuscaParticCiaAb.aspx?CNPJNome=&TipoConsult=C"
        self.engine = create_engine("sqlite:///banco.db", echo=True)
    def get_table(self):
        df = pd.read_html(self.URL)[0]
        df.columns = ["CNPJ", "NOME", "TIPO", "CÓDIGO", "SITUAÇÃO"]
        df.drop(df.head(1).index, inplace=True)
        return df[df.SITUAÇÃO.str.startswith('Concedido')]
    
    def save(self):
        self.get_table().to_sql("Code_cvm", con=self.engine, if_exists="replace", index=False)


if __name__ == '__main__':
    code = CodeCvm()
    print(code.get_table())