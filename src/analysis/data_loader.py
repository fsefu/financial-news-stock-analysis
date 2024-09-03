
import pandas as pd
import os

class DataLoader:
    def __init__(self, news_data_path: str, stock_data_dir: str):
        self.news_data_path = news_data_path
        self.stock_data_dir = stock_data_dir

    def load_news_data(self) -> pd.DataFrame:
        """Loads and returns the news data from a CSV file."""
        try:
            news_data = pd.read_csv(self.news_data_path)
            return news_data
        except FileNotFoundError as e:
            print(f"Error loading news data: {e}")
            return pd.DataFrame()

    def load_stock_data(self, ticker: str) -> pd.DataFrame:
        """Loads stock data for a given ticker symbol from a CSV file."""
        file_path = os.path.join(self.stock_data_dir, f"{ticker}_historical_data.csv")
        try:
            stock_data = pd.read_csv(file_path)
            return stock_data
        except FileNotFoundError as e:
            print(f"Error loading stock data for {ticker}: {e}")
            return pd.DataFrame()

    def load_all_stock_data(self) -> dict:
        """Loads all stock data from the stock_data_dir."""
        stock_data = {}
        for file_name in os.listdir(self.stock_data_dir):
            if file_name.endswith('.csv'):
                ticker = file_name.split('_')[0]
                stock_data[ticker] = self.load_stock_data(ticker)
        return stock_data
