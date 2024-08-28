import pandas as pd

class HeadlineAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze_headline_length(self):
        self.data['headline_length'] = self.data['headline'].apply(len)
        length_stats = self.data['headline_length'].describe()
        return length_stats

    def count_articles_per_publisher(self):
        publisher_counts = self.data['publisher'].value_counts()
        return publisher_counts

    def analyze_publication_dates(self):
        self.data['date'] = pd.to_datetime(self.data['date'])
        date_trends = self.data['date'].dt.date.value_counts().sort_index()
        return date_trends
