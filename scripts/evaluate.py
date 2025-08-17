import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, RegressionPreset
import os

def evaluate_model():
    """Evaluate the model and generate a report."""
    # Load the test data
    test_df = pd.read_csv('include/data/processed/test.csv')
    train_df = pd.read_csv('include/data/processed/train.csv')

    # Load the model
    model = joblib.load('include/models/linear_regression.pkl')

    # Prepare the test data
    X_test = test_df.drop('MedHouseVal', axis=1)
    y_test = test_df['MedHouseVal']

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    # Create directories if they don't exist
    os.makedirs('include/reports', exist_ok=True)

    # Generate Evidently AI report
    report = Report(metrics=[
        DataDriftPreset(),
        RegressionPreset(),
    ])

    # Prepare data for the report
    train_df['prediction'] = model.predict(train_df.drop('MedHouseVal', axis=1))
    test_df['prediction'] = predictions

    report.run(reference_data=train_df, current_data=test_df)

    # Save the report
    report.save_html('include/reports/evidently_report.html')

if __name__ == '__main__':
    evaluate_model()
