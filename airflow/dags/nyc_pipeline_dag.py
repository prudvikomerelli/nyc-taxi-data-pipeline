from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1)
}

with DAG('nyc_taxi_etl', schedule_interval=None, default_args=default_args, catchup=False) as dag:

    run_spark_etl = BashOperator(
        task_id='run_spark_etl',
        bash_command='/opt/spark/bin/spark-submit /spark/spark_etl.py'
    )
