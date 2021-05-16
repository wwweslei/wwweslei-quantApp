import unittest

from quantApp.ext.theoretical_portfolio_ibov import firefox, URL


class test_portfolio_ibov(unittest.TestCase):
    def setUp(self):
        self.firefox = firefox

    def tearDown(self):
        self.firefox.quit()

    def test_title_indices(self):
        self.assertEqual(firefox.title, "Índices", f"page Error title= {firefox.title}")

