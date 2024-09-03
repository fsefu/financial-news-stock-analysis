# tests/sentiment_correlation_analysis/test_sentiment_analyzer.py

import os
import sys
import unittest

# Include path to the source code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from analysis.sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.sentiment_analyzer = SentimentAnalyzer()
    
    def test_analyze_sentiment_positive(self):
        headline = "Stock prices are expected to rise"
        sentiment_score = self.sentiment_analyzer.analyze_sentiment(headline)
        self.assertGreater(sentiment_score, 0, "Sentiment should be positive for this headline")
    
    def test_analyze_sentiment_negative(self):
        headline = "Market crashes due to economic downturn"
        sentiment_score = self.sentiment_analyzer.analyze_sentiment(headline)
        self.assertLess(sentiment_score, 0, "Sentiment should be negative for this headline")
    
    def test_analyze_sentiment_neutral(self):
        headline = "Company announces quarterly earnings"
        sentiment_score = self.sentiment_analyzer.analyze_sentiment(headline)
        self.assertAlmostEqual(sentiment_score, 0, delta=0.1, msg="Sentiment should be neutral for this headline")

if __name__ == "__main__":
    unittest.main()
