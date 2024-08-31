from textblob import TextBlob
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SentimentAnalysis:
    def __init__(self, data):
        self.data = data

    def perform_sentiment_analysis(self):
        self.data['sentiment'] = self.data['headline'].apply(self._get_sentiment)
        sentiment_summary = self.data['sentiment'].value_counts()
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.countplot(x=self.data['sentiment'], palette='coolwarm')
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Number of Headlines')
        plt.grid(True)
        plt.show()
        
        return sentiment_summary

    def _get_sentiment(self, text):
        analysis = TextBlob(text)
        return 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'

    def extract_common_keywords(self):
        all_words = ' '.join(self.data['headline']).lower().split()
        common_words = Counter(all_words).most_common(10)
        
        # Visualization
        keywords, counts = zip(*common_words)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(counts), y=list(keywords), palette='magma')
        plt.title('Top 10 Common Keywords in Headlines')
        plt.xlabel('Frequency')
        plt.ylabel('Keyword')
        plt.grid(True)
        plt.show()
        
        return common_words
