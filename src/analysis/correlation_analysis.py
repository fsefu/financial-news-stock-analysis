import pandas as pd
from scipy.stats import pearsonr

class CorrelationAnalysis:
    def __init__(self, sentiment_df, stock_df):
        self.sentiment_df = sentiment_df
        self.stock_df = stock_df

    def calculate_daily_returns(self):
        """
        Calculates the daily returns of stock prices.

        Returns:
        pd.DataFrame: DataFrame with an additional 'daily_return' column.
        """
        if 'Close' in self.stock_df.columns:
            self.stock_df.rename(columns={'Close': 'close'}, inplace=True)
        
        self.stock_df['daily_return'] = self.stock_df['close'].pct_change()
        return self.stock_df
    
    def compute_correlation(self):
        """
        Computes the correlation between sentiment scores and daily stock returns.

        Returns:
        float: Pearson correlation coefficient.
        """
        if 'Date' in self.sentiment_df.columns:
            self.sentiment_df.rename(columns={'Date': 'date'}, inplace=True)
        if 'Date' in self.stock_df.columns:
            self.stock_df.rename(columns={'Date': 'date'}, inplace=True)
        
        merged_df = pd.merge(self.sentiment_df, self.stock_df, on='date')
        
        # Debugging output
        print("Merged DataFrame Head:\n", merged_df.head())
        print("Missing Values:\n", merged_df[['sentiment_score', 'daily_return']].isna().sum())
        print("Standard Deviations:\n", merged_df[['sentiment_score', 'daily_return']].std())
        
        correlation, _ = pearsonr(merged_df['sentiment_score'].dropna(), merged_df['daily_return'].dropna())
        return correlation


# import pandas as pd
# from scipy.stats import pearsonr

# class CorrelationAnalysis:
#     def __init__(self, sentiment_df, stock_df):
#         self.sentiment_df = sentiment_df
#         self.stock_df = stock_df

#     def calculate_daily_returns(self):
#         """
#         Calculates the daily returns of stock prices.

#         Returns:
#         pd.DataFrame: DataFrame with an additional 'daily_return' column.
#         """
#         # Rename column if needed
#         if 'Close' in self.stock_df.columns:
#             self.stock_df.rename(columns={'Close': 'close'}, inplace=True)
        
#         self.stock_df['daily_return'] = self.stock_df['close'].pct_change()
#         return self.stock_df
    
#     def compute_correlation(self):
#         """
#         Computes the correlation between sentiment scores and daily stock returns.

#         Returns:
#         float: Pearson correlation coefficient.
#         """
#         # Ensure both DataFrames have 'date' column renamed
#         if 'Date' in self.sentiment_df.columns:
#             self.sentiment_df.rename(columns={'Date': 'date'}, inplace=True)
#         if 'Date' in self.stock_df.columns:
#             self.stock_df.rename(columns={'Date': 'date'}, inplace=True)
        
#         merged_df = pd.merge(self.sentiment_df, self.stock_df, on='date')
#         correlation, _ = pearsonr(merged_df['sentiment_score'], merged_df['daily_return'])
#         return correlation
