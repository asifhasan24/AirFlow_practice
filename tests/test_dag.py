import pytest
from airflow.models.dagbag import DagBag


def test_dag_integrity():
    """Test the integrity of the DAG."""
    dag_bag = DagBag(dag_folder='dags', include_examples=False)
    assert not dag_bag.import_errors
