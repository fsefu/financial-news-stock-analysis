from datetime import datetime
import pandas as pd

class DateUtils:
    @staticmethod
    def align_dates(news_df, stock_df):
        """
        Aligns the news and stock data by date.
        
        Parameters:
        news_df (pd.DataFrame): DataFrame containing news articles.
        stock_df (pd.DataFrame): DataFrame containing stock prices.

        Returns:
        pd.DataFrame, pd.DataFrame: Aligned news and stock dataframes.
        """
        # Rename columns to ensure consistency
        if 'Date' in news_df.columns:
            news_df.rename(columns={'Date': 'date'}, inplace=True)
        if 'Date' in stock_df.columns:
            stock_df.rename(columns={'Date': 'date'}, inplace=True)

        # Convert date columns to datetime and extract date only
        news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce').dt.date
        stock_df['date'] = pd.to_datetime(stock_df['date'], errors='coerce').dt.date
        
        # Drop rows where the date conversion failed
        news_df = news_df.dropna(subset=['date'])
        stock_df = stock_df.dropna(subset=['date'])
        
        # Filter only matching dates
        common_dates = news_df['date'].unique()
        news_df = news_df[news_df['date'].isin(common_dates)]
        stock_df = stock_df[stock_df['date'].isin(common_dates)]
        
        return news_df, stock_df
