import pandas as pd

class StockAnalysis:
    def calculate_daily_returns(self, stock_data: pd.DataFrame) -> pd.DataFrame:
        """Calculates daily returns from the stock price data."""
        stock_data['Daily Return'] = stock_data['Close'].pct_change()
        return stock_data

    def merge_data(self, news_data: pd.DataFrame, stock_data: pd.DataFrame) -> pd.DataFrame:
        """Merges news data with stock data on date, handling date parsing robustly."""
        
        # Convert 'Date' in stock_data and 'date' in news_data to datetime, handling errors
        stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce').dt.date
        news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce').dt.date
        
        # Drop rows with NaT values in date columns after coercion
        stock_data = stock_data.dropna(subset=['Date'])
        news_data = news_data.dropna(subset=['date'])

        # Merge the two datasets on date
        merged_data = pd.merge(news_data, stock_data, left_on='date', right_on='Date', how='inner')
        return merged_data

    def calculate_correlation(self, merged_data: pd.DataFrame) -> float:
        """Calculates the correlation between sentiment scores and daily stock returns."""
        correlation = merged_data['Sentiment'].corr(merged_data['Daily Return'])
        return correlation
