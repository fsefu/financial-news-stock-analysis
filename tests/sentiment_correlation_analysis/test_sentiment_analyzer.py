import unittest

import os
import sys

# Include path to the source code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from analysis.sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.sentiment_analyzer = SentimentAnalyzer()

    def test_analyze_sentiment_positive(self):
        # Test positive sentiment
        sentiment = self.sentiment_analyzer.analyze_sentiment("This is a great product")
        self.assertGreater(sentiment, 0, "Sentiment score should be positive for a positive statement")

    def test_analyze_sentiment_negative(self):
        # Test negative sentiment
        sentiment = self.sentiment_analyzer.analyze_sentiment("This is a terrible product")
        self.assertLess(sentiment, 0, "Sentiment score should be negative for a negative statement")

    def test_analyze_sentiment_neutral(self):
        # Test neutral sentiment
        sentiment = self.sentiment_analyzer.analyze_sentiment("This is a product")
        self.assertEqual(sentiment, 0, "Sentiment score should be zero for a neutral statement")

if __name__ == '__main__':
    unittest.main()
