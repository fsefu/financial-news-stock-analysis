import yfinance as yf
import pandas as pd
import numpy as np

class FinancialMetrics:
    def __init__(self, data):
        self.data = data

    def calculate_sharpe_ratio(self, risk_free_rate=0.0):
        """Calculates the Sharpe Ratio."""
        # Calculate daily returns
        self.data['Daily_Return'] = self.data['Close'].pct_change()
        
        # Calculate the excess returns by subtracting the risk-free rate
        excess_return = self.data['Daily_Return'] - risk_free_rate
        
        # Calculate the mean and standard deviation of the excess returns
        mean_excess_return = excess_return.mean()
        std_excess_return = excess_return.std()
        
        # Calculate the Sharpe Ratio
        sharpe_ratio = mean_excess_return / std_excess_return
        return sharpe_ratio
