import os
import sys
import unittest
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from eda.time_series_analysis import TimeSeriesAnalysis

class TestTimeSeriesAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        print("testing  TimeSeriesAnalysis class")

        self.sample_data = pd.DataFrame({
            'headline': [
                'Stock market hits new highs',
                'Earnings report shows growth',
                'Company X announces new product'
            ],
            'publisher': ['Publisher A', 'Publisher B', 'Publisher A'],
            'date': ['2024-08-25', '2024-08-25', '2024-08-26']
        })

        self.analysis = TimeSeriesAnalysis(self.sample_data)
        

    def test_analyze_publication_frequency(self):
        # Test the analysis of publication frequency over time
        publication_frequency = self.analysis.analyze_publication_frequency()
        self.assertEqual(publication_frequency['2024-08-25'], 2)
        self.assertEqual(publication_frequency['2024-08-26'], 1)

    def test_analyze_publisher_contributions(self):
        # Test the analysis of publisher contributions
        publisher_contributions = self.analysis.analyze_publisher_contributions()
        self.assertEqual(publisher_contributions['Publisher A'], 2)
        self.assertEqual(publisher_contributions['Publisher B'], 1)

if __name__ == '__main__':
    unittest.main()
