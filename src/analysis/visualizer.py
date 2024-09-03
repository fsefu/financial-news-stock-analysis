
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def plot_correlation(self, merged_data: pd.DataFrame):
        """Plots a scatter plot showing the correlation between sentiment scores and daily stock returns."""
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Sentiment', y='Daily Return', data=merged_data)
        plt.title('Correlation between Sentiment Scores and Daily Stock Returns')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Daily Return')
        plt.axhline(0, color='red', linestyle='--', linewidth=1)
        plt.axvline(0, color='red', linestyle='--', linewidth=1)
        plt.show()
