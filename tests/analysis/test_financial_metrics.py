import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from metrics.financial_metrics import FinancialMetrics
class TestFinancialMetrics(unittest.TestCase):

    def setUp(self):
        self.data = pd.read_csv('../../data/yfinance_data/TSLA_historical_data.csv')
        self.metrics = FinancialMetrics(self.data)

    def test_calculate_sharpe_ratio(self):
        sharpe_ratio = self.metrics.calculate_sharpe_ratio()
        self.assertIsInstance(sharpe_ratio, float, "Sharpe Ratio should be a float.")
        self.assertNotEqual(sharpe_ratio, 0, "Sharpe Ratio should not be zero.")

if __name__ == '__main__':
    unittest.main()