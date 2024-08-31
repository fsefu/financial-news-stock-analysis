import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TimeSeriesAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze_publication_frequency(self):
        self.data['date'] = pd.to_datetime(self.data['date'], utc=True)  # or dt.tz_localize(None)
        time_series = self.data.set_index('date').resample('D').size()
        
        # Visualization
        plt.figure(figsize=(10, 6))
        time_series.plot(kind='line')
        plt.title('Publication Frequency Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.grid(True)
        plt.show()
        
        return time_series

    def analyze_publisher_contributions(self):
        publisher_contributions = self.data.groupby('publisher')['headline'].count()
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.barplot(x=publisher_contributions.index, y=publisher_contributions.values, palette='plasma')
        plt.title('Publisher Contributions')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.show()
        
        return publisher_contributions
