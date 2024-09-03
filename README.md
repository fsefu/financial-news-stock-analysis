# **Financial News Headline and Stock Analysis**

## **Overview**

This project extends the analysis of financial news headlines to correlate the sentiment derived from these headlines with actual stock price movements. It includes Exploratory Data Analysis (EDA), sentiment analysis, time series analysis, and correlation analysis between news sentiment and stock performance.

## **Table of Contents**

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results and Visualizations](#results-and-visualizations)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## **Features**

- **Data Cleaning**: Preprocess and clean raw data to ensure consistency and accuracy.
- **Headline Analysis**: Analyze the length of headlines, count articles per publisher, and observe publication date trends.
- **Sentiment Analysis**: Perform sentiment analysis on headlines to classify them as positive, negative, or neutral. Extract common keywords from the text.
- **Time Series Analysis**: Analyze the frequency of publications over time and contributions by different publishers.
- **Stock Price Analysis**: Calculate daily stock returns based on closing prices.
- **Sentiment-Stock Correlation**: Merge news sentiment data with stock price data to calculate the correlation between sentiment scores and stock price movements.
- **Visualization**: Generate insightful visualizations to better understand the dataset, stock performance, and correlations.

## **Project Structure**

```plaintext
Financial-News-Stock-Analysis/
├── .github/                # GitHub-specific configuration files
├── .vscode/                # VSCode-specific configuration files
├── .wvenv/                 # Python virtual environment files
├── data/                   # Directory containing raw data files
│   ├── raw_analyst_ratings.csv
│   └── yfinance_data/      # Directory for historical stock price files
│       ├── AAPL_historical_data.csv
│       ├── GOOG_historical_data.csv
│       ├── MSFT_historical_data.csv
│       └── TSLA_historical_data.csv
├── notebooks/              # Jupyter notebook for running the analysis
│   └── analysis_notebook.ipynb
├── scripts/                # Utility scripts for data cleaning
│   └── data_cleaner.py
├── src/                    # Source directory for analysis modules
│   ├── analysis/           # Analysis modules for stock and sentiment analysis
│   │   ├── data_loader.py
│   │   ├── sentiment_analyzer.py
│   │   ├── stock_analysis.py
│   │   └── visualizer.py
│   └── tests/              # Unit test modules for testing analysis functionality
│       ├── __init__.py
│       └── sentiment_correlation_analysis/
│           ├── __init__.py
│           ├── test_data_loader.py
│           ├── test_sentiment_analyzer.py
│           ├── test_stock_analysis.py
│           └── test_visualizer.py
├── Dockerfile              # Docker configuration for containerized environment
├── docker-compose.yml      # Docker Compose configuration file
├── README.md               # Project README file
├── requirements.txt        # Python dependencies
└── LICENSE                 # License file
```


## **Installation**

### **Prerequisites**

Ensure you have the following installed:

- Python 3.7 or later
- Jupyter Notebook
- Docker (optional, for containerization)

### **Installing Dependencies**

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/financial-news-stock-analysis.git
    cd financial-news-stock-analysis
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Set up a virtual environment:

    ```bash
    python -m venv .wvenv
    source .wvenv/bin/activate  # On Windows: .wvenv\Scripts\activate
    ```

## **Usage**

### **Running the Jupyter Notebook**

To explore the analysis interactively:

1. Start Jupyter Notebook:

    ```bash
    jupyter notebook notebooks/analysis_notebook.ipynb
    ```

2. Run the cells sequentially to perform data cleaning, headline analysis, sentiment analysis, time series analysis, stock price analysis, and correlation analysis.

### **Running the Analysis Scripts**

You can also run the analysis scripts directly for non-interactive use:

    ```python
    from src.analysis.data_loader import DataLoader
    from src.analysis.sentiment_analyzer import SentimentAnalyzer
    from src.analysis.stock_analysis import StockAnalysis
    from src.analysis.visualizer import Visualizer

    # Initialize data loader
    data_loader = DataLoader(news_data_path='data/raw_analyst_ratings.csv', stock_data_dir='data/yfinance_data')

    # Load data
    news_data = data_loader.load_news_data()
    stock_data = data_loader.load_stock_data(ticker='AAPL')

    # Perform sentiment analysis
    sentiment_analyzer = SentimentAnalyzer()
    news_data['Sentiment'] = news_data['headline'].apply(sentiment_analyzer.analyze_sentiment)

    # Calculate daily stock returns
    stock_analysis = StockAnalysis()
    stock_data = stock_analysis.calculate_daily_returns(stock_data)

    # Merge data and calculate correlation
    merged_data = stock_analysis.merge_data(news_data, stock_data)
    correlation = stock_analysis.calculate_correlation(merged_data)

    # Visualize the correlation
    visualizer = Visualizer()
    visualizer.plot_correlation(merged_data)
    ```

## **Results and Visualizations**

The project provides several key visualizations, including:

- **Distribution of Headline Lengths**
- **Number of Articles per Publisher**
- **Publication Date Trends**
- **Sentiment Distribution**
- **Top 10 Common Keywords in Headlines**
- **Publication Frequency Over Time**
- **Publisher Contributions**
- **Correlation between Sentiment Scores and Daily Stock Returns**

These visualizations help to uncover patterns and trends in the dataset, providing valuable insights into the financial news headlines and their impact on stock prices.

## **Technologies Used**

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **TextBlob**: Sentiment analysis
- **Jupyter Notebook**: Interactive environment for data analysis
- **Docker**: Containerization

## **Contributing**

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Contact**

For any questions or feedback, feel free to reach out:

- **Email**: sefuwanfd@gmail.com
- **GitHub**: [fsefu](https://github.com/fsefu)
- **LinkedIn**: [Sefuwan Feysa](https://www.linkedin.com/in/sefuwanf/)
