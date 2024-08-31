import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class HeadlineAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze_headline_length(self):
        self.data['headline_length'] = self.data['headline'].apply(len)
        length_stats = self.data['headline_length'].describe()
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['headline_length'], bins=20, kde=True)
        plt.title('Distribution of Headline Lengths')
        plt.xlabel('Headline Length')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
        
        return length_stats

    def count_articles_per_publisher(self):
        publisher_counts = self.data['publisher'].value_counts()
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.barplot(x=publisher_counts.index, y=publisher_counts.values, palette='viridis')
        plt.title('Number of Articles per Publisher')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.show()
        
        return publisher_counts

    def analyze_publication_dates(self):
        self.data['date'] = pd.to_datetime(self.data['date'])
        date_trends = self.data['date'].dt.date.value_counts().sort_index()
        
        # Visualization
        plt.figure(figsize=(10, 6))
        date_trends.plot(kind='line')
        plt.title('Publication Date Trends')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.grid(True)
        plt.show()
        
        return date_trends
