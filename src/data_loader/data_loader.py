import pandas as pd

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None

    def load_data(self):
        """Loads the data from the given CSV file."""
        self.data = pd.read_csv(self.data_path)
        self.prepare_data()
        return self.data

    def prepare_data(self):
        """Prepares and cleans the stock data."""
        expected_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        if not all(column in self.data.columns for column in expected_columns):
            raise ValueError("Data must contain Date, Open, High, Low, Close, and Volume columns.")

        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        self.data.dropna(inplace=True)
