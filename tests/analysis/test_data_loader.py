import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from data_loader.data_loader import DataLoader
class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        data_loader = DataLoader('../../data/yfinance_data/TSLA_historical_data.csv')
        data = data_loader.load_data()

        self.assertIsInstance(data, pd.DataFrame, "Loaded data should be a DataFrame.")
        self.assertFalse(data.empty, "Loaded data should not be empty.")
        self.assertTrue(all(column in data.columns for column in ['Open', 'High', 'Low', 'Close', 'Volume']),
                        "Data should contain all expected columns.")

    def test_prepare_data_missing_column(self):
        data_loader = DataLoader('tests/test_data/missing_columns.csv')
        
        with self.assertRaises(ValueError) as context:
            data_loader.load_data()
        
        self.assertTrue("Data must contain Date, Open, High, Low, Close, and Volume columns." in str(context.exception))

    def test_date_conversion_and_cleaning(self):
        data_loader = DataLoader('../../data/yfinance_data/TSLA_historical_data.csv')
        data = data_loader.load_data()
        
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(data.index), "Date column should be converted to datetime.")
        self.assertEqual(data.isnull().sum().sum(), 0, "Data should not contain any NaN values after cleaning.")

if __name__ == '__main__':
    unittest.main()