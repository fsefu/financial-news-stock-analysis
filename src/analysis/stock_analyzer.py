from src.data.data_loader import DataLoader
from src.indicators.technical_indicators import TechnicalIndicators
from src.metrics.financial_metrics import FinancialMetrics
from src.eda.visualizer import Visualizer

class StockAnalyzer:
    def __init__(self, data_path):
        self.data_loader = DataLoader(data_path)
        self.data = self.data_loader.load_data()
        self.indicators = TechnicalIndicators(self.data)
        self.metrics = FinancialMetrics(self.data)
        self.visualizer = Visualizer(self.data)

    def run_analysis(self):
        """Runs the complete analysis pipeline."""
        # Calculate Indicators
        self.indicators.calculate_moving_averages()
        self.indicators.calculate_rsi()
        self.indicators.calculate_macd()

        # Calculate Financial Metrics
        sharpe_ratio = self.metrics.calculate_sharpe_ratio()
        print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

        # Visualize
        self.visualizer.plot_moving_averages()
        self.visualizer.plot_rsi()
        self.visualizer.plot_macd()
