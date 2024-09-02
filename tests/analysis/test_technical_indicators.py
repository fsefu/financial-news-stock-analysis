import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from indicators.technical_indicators import TechnicalIndicators

class TestTechnicalIndicators(unittest.TestCase):

    def setUp(self):
        self.data = pd.read_csv('../../data/yfinance_data/TSLA_historical_data.csv')
        self.indicators = TechnicalIndicators(self.data)

    def test_calculate_moving_averages(self):
        self.indicators.calculate_moving_averages()
        self.assertIn('MA50', self.data.columns, "MA50 should be in the DataFrame after calculation.")
        self.assertIn('MA200', self.data.columns, "MA200 should be in the DataFrame after calculation.")

    def test_calculate_rsi(self):
        self.indicators.calculate_rsi()
        self.assertIn('RSI', self.data.columns, "RSI should be in the DataFrame after calculation.")

    def test_calculate_macd(self):
        self.indicators.calculate_macd()
        self.assertIn('MACD', self.data.columns, "MACD should be in the DataFrame after calculation.")
        self.assertIn('MACD_signal', self.data.columns, "MACD_signal should be in the DataFrame after calculation.")
        self.assertIn('MACD_hist', self.data.columns, "MACD_hist should be in the DataFrame after calculation.")

if __name__ == '__main__':
    unittest.main()