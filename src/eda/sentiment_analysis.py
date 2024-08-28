# src/eda/sentiment_analysis.py

from textblob import TextBlob
from collections import Counter
import pandas as pd

class SentimentAnalysis:
    def __init__(self, data):
        self.data = data

    def perform_sentiment_analysis(self):
        self.data['sentiment'] = self.data['headline'].apply(self._get_sentiment)
        sentiment_summary = self.data['sentiment'].value_counts()
        return sentiment_summary

    def _get_sentiment(self, text):
        analysis = TextBlob(text)
        return 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'

    def extract_common_keywords(self):
        all_words = ' '.join(self.data['headline']).lower().split()
        common_words = Counter(all_words).most_common(10)
        return common_words
