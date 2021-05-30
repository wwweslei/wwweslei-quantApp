import unittest
import pandas as pd
from sqlalchemy import create_engine
from quantAPP.ext.cvm_cod import CodeCvm


class test_portfolio_ibov(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        code_cvm = CodeCvm()
        cls.df_update = code_cvm.get_table()


    def setUp(self):
        self.engine = create_engine("sqlite:///banco.db")
        self.df = pd.read_sql("select * from Code_cvm", self.engine)

    def test_ambev_in_ibov(self):
        a = self.df["NOME"]
        self.assertEqual(a[0], "2W ENERGIA S.A.")

    def test_min_len_column(self):
        self.assertTrue(len(self.df) > 720)

    def test_max_len_column(self):
        self.assertTrue(len(self.df) < 900)

    def test_update_table(self):
        self.assertEqual(len(self.df), len(self.df_update))


if __name__ == "__main__":
    unittest.main(verbosity=2)
