import unittest
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from quantAPP.ext.empresas_listadas_ibov import BuscaEmpresaListada


class test_portfolio_ibov(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        empresas = BuscaEmpresaListada()
        cls.df_update = empresas.get_table()

    def setUp(self):
        self.engine = create_engine("sqlite:///banco.db")
        self.df = pd.read_sql("select * from empresas", self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.table = self.session.execute("select * from empresas")

    def tearDown(self):
        self.session.close()

    def test_3r_Petroleum_in_empresas(self):
        self.assertEqual(self.df["Razão Social"][0], "3R PETROLEUM ÓLEO E GÁS S.A")

    def test_min_len_column(self):
        self.assertTrue(len(self.df) > 400)

    def test_max_len_column(self):
        self.assertTrue(len(self.df) < 500)

    def test_equal_df_and_db(self):
        self.assertEqual(len(self.df), len([x for x in self.table]))

    def test_update_table(self):
        self.assertEqual(len(self.df), len(self.df_update))


if __name__ == "__main__":
    unittest.main(verbosity=2)
