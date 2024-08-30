# **Financial News Headline Analysis**

## **Overview**

This project is designed to perform Exploratory Data Analysis (EDA) on a dataset of financial news headlines. The goal is to extract meaningful insights and patterns from the data, which includes headline analysis, sentiment analysis, and time series analysis.

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
- **Visualization**: Generate insightful visualizations to better understand the dataset and its characteristics.

## **Project Structure**

```plaintext
Financial-News-Headline-Analysis/
├── .github/                # GitHub-specific configuration files
├── .vscode/                # VSCode-specific configuration files
├── .venv/                  # Python virtual environment files
├── data/                   # Directory containing raw data files
│   └── raw_analyst_ratings.csv
├── notebooks/              # Jupyter notebook for running the analysis
│   └── eda_notebook.ipynb
├── scripts/                # Utility scripts for data cleaning
│   └── data_cleaner.py
├── src/                    # Source directory for analysis modules
│   ├── analysis/           # (Reserved for future analysis modules)
│   ├── eda/                # EDA modules for headline, sentiment, and time series analysis
│   │   ├── headline_analysis.py
│   │   ├── sentiment_analysis.py
│   │   └── time_series_analysis.py
│   └── tests/              # (Reserved for future test modules)
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
   git clone https://github.com/your-username/financial-news-headline-analysis.git
   cd financial-news-headline-analysis
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

## **Usage**

### **Running the Jupyter Notebook**

To explore the analysis interactively:

1. Start Jupyter Notebook:

   ```bash
   jupyter notebook notebooks/eda_notebook.ipynb
   ```

2. Run the cells sequentially to perform data cleaning, headline analysis, sentiment analysis, and time series analysis.

### **Running the Analysis Scripts**

You can also run the analysis scripts directly for non-interactive use:

```python
from scripts.data_cleaner import DataCleaner
from src.eda.headline_analysis import HeadlineAnalysis
from src.eda.sentiment_analysis import SentimentAnalysis
from src.eda.time_series_analysis import TimeSeriesAnalysis

# Load your data (example)
data = pd.read_csv('data/raw_analyst_ratings.csv')

# Clean the data
cleaner = DataCleaner(data)
cleaned_data = cleaner.clean_dates()

# Perform headline analysis
headline_analyzer = HeadlineAnalysis(cleaned_data)
headline_stats = headline_analyzer.analyze_headline_length()
publisher_counts = headline_analyzer.count_articles_per_publisher()
date_trends = headline_analyzer.analyze_publication_dates()

# Perform sentiment analysis
sentiment_analyzer = SentimentAnalysis(cleaned_data)
sentiment_summary = sentiment_analyzer.perform_sentiment_analysis()
common_keywords = sentiment_analyzer.extract_common_keywords()

# Perform time series analysis
time_series_analyzer = TimeSeriesAnalysis(cleaned_data)
publication_frequency = time_series_analyzer.analyze_publication_frequency()
publisher_contributions = time_series_analyzer.analyze_publisher_contributions()
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

These visualizations help to uncover patterns and trends in the dataset, providing valuable insights into the financial news headlines.

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
