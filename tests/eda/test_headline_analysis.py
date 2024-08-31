from datetime import datetime
import os
import sys
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from eda.headline_analysis import HeadlineAnalysis

class TestHeadlineAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_data = pd.DataFrame({
            'headline': [
                'Stock market hits new highs',
                'Earnings report shows growth',
                'Company X announces new product'
            ],
            'publisher': ['Publisher A', 'Publisher B', 'Publisher A'],
            'date': ['2024-08-25', '2024-08-25', '2024-08-26']
        })
        self.analysis = HeadlineAnalysis(self.sample_data)

    def test_analyze_headline_length(self):
        # Test the analysis of headline lengths
        length_stats = self.analysis.analyze_headline_length()
        self.assertEqual(length_stats['count'], 3)
        self.assertGreater(length_stats['mean'], 0)

    def test_count_articles_per_publisher(self):
        # Test the counting of articles per publisher
        publisher_counts = self.analysis.count_articles_per_publisher()
        self.assertEqual(publisher_counts['Publisher A'], 2)
        self.assertEqual(publisher_counts['Publisher B'], 1)

    def test_analyze_publication_dates(self):
        # Test the analysis of publication dates
        date_trends = self.analysis.analyze_publication_dates()
        print("date_trends: ", date_trends)
        print("Available Keys:", list(date_trends.keys()))

        # Convert the test date strings to datetime.date objects
        date_2024_08_25 = datetime.strptime('2024-08-25', '%Y-%m-%d').date()
        date_2024_08_26 = datetime.strptime('2024-08-26', '%Y-%m-%d').date()

        self.assertEqual(date_trends[date_2024_08_25], 2)
        self.assertEqual(date_trends[date_2024_08_26], 1)

if __name__ == '__main__':
    unittest.main()
