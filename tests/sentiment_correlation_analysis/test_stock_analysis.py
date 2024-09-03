import unittest
import pandas as pd
from analysis.stock_analysis import StockAnalysis

class TestStockAnalysis(unittest.TestCase):

    def setUp(self):
        self.stock_analysis = StockAnalysis()
        # Sample data
        self.news_data = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'headline': ['Good news', 'Bad news', 'Neutral news'],
            'Sentiment': [0.5, -0.5, 0.0]
        })
        self.stock_data = pd.DataFrame({
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'Close': [100, 102, 101]
        })

    def test_calculate_daily_returns(self):
        """Test the calculation of daily returns."""
        result = self.stock_analysis.calculate_daily_returns(self.stock_data.copy())
        self.assertIn('Daily Return', result.columns)
        self.assertAlmostEqual(result['Daily Return'].iloc[1], 0.02, places=7)  # Compare up to 7 decimal places


    def test_merge_data(self):
        """Test merging of news and stock data."""
        self.stock_data = self.stock_analysis.calculate_daily_returns(self.stock_data.copy())
        result = self.stock_analysis.merge_data(self.news_data, self.stock_data)
        self.assertIn('Daily Return', result.columns)
        self.assertIn('Sentiment', result.columns)
        self.assertEqual(len(result), 3)

    def test_calculate_correlation(self):
        """Test correlation calculation between sentiment and daily returns."""
        self.stock_data = self.stock_analysis.calculate_daily_returns(self.stock_data.copy())
        merged_data = self.stock_analysis.merge_data(self.news_data, self.stock_data)
        correlation = self.stock_analysis.calculate_correlation(merged_data)
        self.assertIsNotNone(correlation)
        self.assertIsInstance(correlation, float)

if __name__ == '__main__':
    unittest.main()
