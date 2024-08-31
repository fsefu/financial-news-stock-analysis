import os
import sys
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from eda.sentiment_analysis import SentimentAnalysis

class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_data = pd.DataFrame({
            'headline': [
                'Stocks That Hit 52-Week Highs On Friday',
                'Stocks That Hit 52-Week Highs On Wednesday',
                'Axcelis Tech Announces Significant Order for High-Performance Upgrade',
                "Barrick Gold Corp. Reports Temporary Suspension Of Operations At Veladero Mine Due To Inspections Of Mine's Heap Leach Area, Company Believes It Will Not Have Any Material Impact To 2016 Guidance At This Time"
            ],
            'publisher': ['Benzinga Insights', 'Benzinga Insights', 'Paul Quintaro', 'Paul Quintaro'],
            'date': ['2020-06-05', '2020-06-03', '5-16-2013', '9-15-2016']
        })
        self.analysis = SentimentAnalysis(self.sample_data)

    def test_perform_sentiment_analysis(self):
        # Test the sentiment analysis of headlines
        sentiment_summary = self.analysis.perform_sentiment_analysis()
        
        # Check expected sentiment counts
        print("sentiment_summary: ", sentiment_summary)
        self.assertEqual(sentiment_summary['neutral'], 2)
        self.assertEqual(sentiment_summary['positive'], 1)
        self.assertEqual(sentiment_summary['negative'], 1)

    def test_extract_common_keywords(self):
        # Test the extraction of common keywords
        common_keywords = self.analysis.extract_common_keywords()

        # Example of expected keywords based on the headlines
        expected_keywords = ['stocks', 'highs', 'friday']

        # Ensure all expected keywords are in the common keywords
        for keyword in expected_keywords:
            self.assertTrue(any(keyword in kw for kw in common_keywords))

if __name__ == '__main__':
    unittest.main()
