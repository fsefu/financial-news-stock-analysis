import talib as ta

class TechnicalIndicators:
    def __init__(self, data):
        self.data = data

    def calculate_moving_averages(self):
        """Calculates moving averages and adds them to the DataFrame."""
        self.data['MA50'] = ta.SMA(self.data['Close'], timeperiod=50)
        self.data['MA200'] = ta.SMA(self.data['Close'], timeperiod=200)

    def calculate_rsi(self):
        """Calculates the RSI and adds it to the DataFrame."""
        self.data['RSI'] = ta.RSI(self.data['Close'], timeperiod=14)

    def calculate_macd(self):
        """Calculates the MACD and adds it to the DataFrame."""
        self.data['MACD'], self.data['MACD_signal'], self.data['MACD_hist'] = ta.MACD(
            self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
