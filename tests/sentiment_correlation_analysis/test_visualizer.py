import unittest
from unittest.mock import patch
import pandas as pd
from analysis.visualizer import Visualizer

class TestVisualizer(unittest.TestCase):

    def setUp(self):
        self.visualizer = Visualizer()
        self.merged_data = pd.DataFrame({
            'Sentiment': [0.5, -0.5, 0.0],
            'Daily Return': [0.02, -0.01, 0.00]
        })

    @patch("matplotlib.pyplot.show")
    def test_plot_correlation(self, mock_show):
        """Test plot_correlation function without displaying the plot."""
        try:
            self.visualizer.plot_correlation(self.merged_data)
            mock_show.assert_called_once()  # Check that plt.show() was called once
        except Exception as e:
            self.fail(f"plot_correlation method failed: {e}")

if __name__ == '__main__':
    unittest.main()
