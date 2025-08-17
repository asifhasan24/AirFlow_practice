# ML Regression Project with Airflow, DVC, and Evidently AI

This project demonstrates a full-fledged MLOps pipeline for a machine learning regression task using Apache Airflow, DVC, and Evidently AI. It also includes a CI/CD pipeline with GitHub Actions.

## Project Overview

The project is structured as follows:

- **dags**: Contains the Airflow DAG for the ML pipeline.
- **include**: Contains data, models, and reports.
- **scripts**: Contains Python scripts for data processing, model training, and evaluation.
- **tests**: Contains tests for the Airflow DAG.
- **.github/workflows**: Contains the CI/CD pipeline configuration.
- **Dockerfile**: For containerizing the project.
- **requirements.txt**: Lists the Python dependencies.
- **README.md**: This file.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up DVC:**

    This project uses DVC to version the data. To get the data, you need to configure a remote storage for DVC. This example uses Google Drive. You can replace it with your preferred storage (S3, Azure Blob Storage, etc.).

    a.  **Configure DVC remote storage:**

        ```bash
        dvc remote add -d myremote gdrive://<your-gdrive-folder-id>
        ```

    b.  **Pull the data:**

        ```bash
        dvc pull
        ```

4.  **Set up Airflow:**

    a.  **Initialize Airflow:**

        ```bash
        airflow db init
        ```

    b.  **Create a user:**

        ```bash
        airflow users create --username admin --password admin --firstname Your --lastname Name --role Admin --email your.email@example.com
        ```

    c.  **Start the Airflow web server and scheduler:**

        ```bash
        airflow webserver --port 8080 &
        airflow scheduler &
        ```

## How to Run the Project

1.  **Access the Airflow UI:**

    Open your web browser and go to `http://localhost:8080`. Log in with the credentials you created.

2.  **Run the DAG:**

    -   In the Airflow UI, you will see the `ml_regression_dag`.
    -   Enable the DAG by clicking the toggle button.
    -   Trigger the DAG manually by clicking the play button.

## CI/CD Pipeline

The project includes a CI/CD pipeline using GitHub Actions. The pipeline is defined in `.github/workflows/ci.yml`. It automatically runs when you push code to the `main` branch. The pipeline performs the following steps:

-   Checks out the code.
-   Installs Python and the project dependencies.
-   Lints the code using `ruff`.
-   Runs the tests using `pytest`.

## DagsHub Integration

DagsHub is a platform for MLOps that combines Git and DVC. To use this project with DagsHub:

1.  Create a new repository on DagsHub.
2.  Follow the instructions on DagsHub to push your Git repository and DVC data.

This will allow you to see your code, data, and experiments in one place.
# AirFlow_practice
