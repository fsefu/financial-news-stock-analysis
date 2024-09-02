import unittest
from unittest.mock import patch
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from analysis.visualizer import Visualizer
class TestVisualizer(unittest.TestCase):

    def setUp(self):
        self.data = pd.read_csv('../../data/yfinance_data/TSLA_historical_data.csv')
        self.visualizer = Visualizer(self.data)

    @patch('matplotlib.pyplot.show')
    def test_plot_moving_averages(self, mock_show):
        self.visualizer.plot_moving_averages()
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_plot_rsi(self, mock_show):
        self.visualizer.plot_rsi()
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_plot_macd(self, mock_show):
        self.visualizer.plot_macd()
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()