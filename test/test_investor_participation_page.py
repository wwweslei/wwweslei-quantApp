import unittest
import pandas as pd
from sqlalchemy import create_engine
from quantAPP.ext.investor_participation_page import InvestorParticipation


class test_portfolio_ibov(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        investor_page = InvestorParticipation()
        cls.df_update = investor_page.get_table()

    def setUp(self):
        self.engine = create_engine("sqlite:///banco.db")
        self.df = pd.read_sql("select * from investorParticipation", self.engine)

    def test_type_investor_in_investor(self):
        a = self.df["Tipo de Investidores"]
        self.assertEqual(a[0], "Investidores Individuais")

    def test_min_len_column(self):
        self.assertTrue(len(self.df) > 6)

    def test_max_len_column(self):
        self.assertTrue(len(self.df) < 8)

    def test_update_table(self):
        self.assertEqual(len(self.df), len(self.df_update))


if __name__ == "__main__":
    unittest.main(verbosity=2)
