from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="ml_regression_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    schedule=None,
    tags=["ml", "regression"],
) as dag:
    dvc_pull = BashOperator(
        task_id="dvc_pull",
        bash_command="dvc pull -f",
    )

    preprocess_data = BashOperator(
        task_id="preprocess_data",
        bash_command="python3 scripts/preprocess.py",
    )

    train_model = BashOperator(
        task_id="train_model",
        bash_command="python3 scripts/train.py",
    )

    evaluate_model = BashOperator(
        task_id="evaluate_model",
        bash_command="python3 scripts/evaluate.py",
    )

    dvc_pull >> preprocess_data >> train_model >> evaluate_model
