# # tests/sentiment_correlation_analysis/test_visualizer.py

# import unittest
# import pandas as pd
# import matplotlib.pyplot as plt
# import os
# import sys

# # Include path to the source code
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
# from analysis.visualizer import Visualizer

# class TestVisualizer(unittest.TestCase):
#     def setUp(self):
#         self.visualizer = Visualizer()
#         self.merged_data = pd.DataFrame({
#             'date': ['2020-01-01', '2020-01-02', '2020-01-03'],
#             'Sentiment': [0.1, -0.2, 0.0],
#             'Daily Return': [0.02, -0.01, 0.03]
#         })
    
#     def test_plot_correlation(self):
#         # Run the plot method
#         self.visualizer.plot_correlation(self.merged_data)
        
#         # Check if the plot was generated
#         self.assertTrue(plt.fignum_exists(1), "The plot should be displayed")
        
#         # Close the plot to prevent interference with other tests
#         plt.close()

# if __name__ == "__main__":
#     unittest.main()
