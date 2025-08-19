from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow!")

with DAG(
    dag_id="example_hello_world",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example"]
) as dag:
    task = PythonOperator(
        task_id="say_hello",
        python_callable=hello_world
    )
