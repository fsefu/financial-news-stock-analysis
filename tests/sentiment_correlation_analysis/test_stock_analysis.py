# tests/sentiment_correlation_analysis/test_stock_analysis.py

import pandas as pd
import os
import sys
import unittest

# Include path to the source code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from analysis.stock_analysis import StockAnalysis

class TestStockAnalysis(unittest.TestCase):
    def setUp(self):
        self.stock_analysis = StockAnalysis()
        self.stock_data = pd.DataFrame({
            'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'Close': [150, 155, 153]
        })
        self.news_data = pd.DataFrame({
            'date': ['2020-01-01', '2020-01-02'],
            'sentiment': [0.1, -0.2]
        })
    
    def test_calculate_daily_returns(self):
        returns = self.stock_analysis.calculate_daily_returns(self.stock_data)
        expected_returns = [None, 0.033333, -0.012903]
        self.assertAlmostEqual(returns['Daily Return'][1], expected_returns[1], places=5)
        self.assertAlmostEqual(returns['Daily Return'][2], expected_returns[2], places=5)
    
    def test_merge_data(self):
        self.stock_data['Date'] = pd.to_datetime(self.stock_data['Date']).dt.date
        self.news_data['date'] = pd.to_datetime(self.news_data['date']).dt.date
        merged_data = self.stock_analysis.merge_data(self.news_data, self.stock_data)
        self.assertEqual(len(merged_data), 2)
        self.assertIn('Sentiment', merged_data.columns)
        self.assertIn('Daily Return', merged_data.columns)
    
    def test_calculate_correlation(self):
        self.stock_data = self.stock_analysis.calculate_daily_returns(self.stock_data)
        merged_data = self.stock_analysis.merge_data(self.news_data, self.stock_data)
        correlation = self.stock_analysis.calculate_correlation(merged_data)
        self.assertTrue(isinstance(correlation, float))

if __name__ == "__main__":
    unittest.main()
