import pandas as pd

class DataCleaner:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def clean_dates(self):
        # Convert the 'date' column to datetime format if not already done
        self.data['date'] = pd.to_datetime(self.data['date'], utc=True)
        
        # Remove the time component, retaining only the date
        self.data['date'] = self.data['date'].dt.date
        print("okayssss")
        # return "OOO"ss
        return self.data