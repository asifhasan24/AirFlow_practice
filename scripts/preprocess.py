import pandas as pd
from sklearn.model_selection import train_test_split
import os

def preprocess_data():
    """Read data, split it into train and test sets, and save them."""
    # Read the dataset
    df = pd.read_csv('include/data/housing.csv')

    # Split the data
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Create directories if they don't exist
    os.makedirs('include/data/processed', exist_ok=True)

    # Save the train and test sets
    train_df.to_csv('include/data/processed/train.csv', index=False)
    test_df.to_csv('include/data/processed/test.csv', index=False)

if __name__ == '__main__':
    preprocess_data()
