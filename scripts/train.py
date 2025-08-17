import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_model():
    """Train a linear regression model and save it."""
    # Load the training data
    train_df = pd.read_csv('include/data/processed/train.csv')

    # Prepare the data
    X_train = train_df.drop('MedHouseVal', axis=1)
    y_train = train_df['MedHouseVal']

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Create directories if they don't exist
    os.makedirs('include/models', exist_ok=True)

    # Save the model
    joblib.dump(model, 'include/models/linear_regression.pkl')

if __name__ == '__main__':
    train_model()
