# src/eda/time_series_analysis.py

import pandas as pd

class TimeSeriesAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze_publication_frequency(self):
        self.data['date'] = pd.to_datetime(self.data['date'])
        time_series = self.data.set_index('date').resample('D').size()
        return time_series

    def analyze_publisher_contributions(self):
        publisher_contributions = self.data.groupby('publisher')['headline'].count()
        return publisher_contributions
