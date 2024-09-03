
from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_sentiment(self, headline: str) -> float:
        """Analyzes sentiment of a headline and returns a sentiment score."""
        analysis = TextBlob(headline)
        return analysis.sentiment.polarity  # returns a float between -1 (negative) and 1 (positive)
