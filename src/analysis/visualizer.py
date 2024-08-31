import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_moving_averages(self):
        """Plots the stock price along with moving averages."""
        plt.figure(figsize=(14, 7))
        plt.plot(self.data.index, self.data['Close'], label='Close Price')
        plt.plot(self.data.index, self.data['MA50'], label='50-day MA', linestyle='--')
        plt.plot(self.data.index, self.data['MA200'], label='200-day MA', linestyle='--')
        plt.title('Stock Price and Moving Averages')
        plt.legend()
        plt.show()

    def plot_rsi(self):
        """Plots the RSI."""
        plt.figure(figsize=(14, 7))
        plt.plot(self.data.index, self.data['RSI'], label='RSI', color='orange')
        plt.axhline(70, color='red', linestyle='--')
        plt.axhline(30, color='green', linestyle='--')
        plt.title('Relative Strength Index (RSI)')
        plt.legend()
        plt.show()

    def plot_macd(self):
        """Plots the MACD and its components."""
        plt.figure(figsize=(14, 7))
        plt.plot(self.data.index, self.data['MACD'], label='MACD', color='blue')
        plt.plot(self.data.index, self.data['MACD_signal'], label='MACD Signal', linestyle='--', color='red')
        plt.fill_between(self.data.index, self.data['MACD_hist'], color='gray', alpha=0.3, label='MACD Histogram')
        plt.title('MACD')
        plt.legend()
        plt.show()
