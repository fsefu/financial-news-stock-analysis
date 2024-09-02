import os
import sys
import unittest
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from src.analysis.stock_analyzer import StockAnalyzer
class TestStockAnalyzer(unittest.TestCase):

    @patch('matplotlib.pyplot.show')
    def test_run_analysis(self, mock_show):
        analyzer = StockAnalyzer('../../data/yfinance_data/TSLA_historical_data.csv')
        analyzer.run_analysis()

        # Verify the plots are displayed
        self.assertEqual(mock_show.call_count, 3)

if __name__ == '__main__':
    unittest.main()