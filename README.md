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
