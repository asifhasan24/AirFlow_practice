import pandas as pd
from sklearn.datasets import fetch_california_housing

def get_data():
    """Fetch California Housing dataset and save it to a CSV file."""
    # Fetch the dataset
    housing = fetch_california_housing()

    # Create a DataFrame
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df['MedHouseVal'] = housing.target

    # Save the DataFrame to a CSV file
    df.to_csv('include/data/housing.csv', index=False)

if __name__ == '__main__':
    get_data()
