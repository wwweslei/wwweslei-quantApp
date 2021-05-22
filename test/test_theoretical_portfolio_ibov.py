import unittest

from quantApp.ext.theoretical_portfolio_ibov import Theoretical_portfolio_ibov


class test_portfolio_ibov(unittest.TestCase):
    def setUp(self):
        self.ibov = Theoretical_portfolio_ibov()
        self.df = self.ibov.scrapy()

    def tearDown(self):
        pass
        

        