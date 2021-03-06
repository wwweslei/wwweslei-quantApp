import unittest
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from quantAPP.ext.theoretical_portfolio_ibov import Theoretical_portfolio_ibov


class test_portfolio_ibov(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ibov = Theoretical_portfolio_ibov()
        cls.df_update = ibov.get_table()

    def setUp(self):
        self.engine = create_engine("sqlite:///banco.db")
        self.df = pd.read_sql("select * from Index_ibov", self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.table = self.session.execute("select * from Index_ibov")

    def tearDown(self):
        self.session.close()

    def test_ambev_in_ibov(self):
        a = self.df["Ação"]
        self.assertEqual(a[0], "AMBEV S/A")

    def test_len_column(self):
        self.assertTrue(len(self.df) > 80)

    def test_equal_df_and_db(self):
        self.assertEqual(len(self.df), len([x for x in self.table]))

    def test_update_table(self):
        self.assertEqual(len(self.df), len(self.df_update))


if __name__ == "__main__":
    unittest.main(verbosity=2)
