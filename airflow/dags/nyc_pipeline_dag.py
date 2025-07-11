from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}

with DAG(
    'nyc_taxi_pipeline',
    default_args=default_args,
    description='ETL DAG for NYC Taxi Data',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
) as dag:

    transform = BashOperator(
        task_id='run_spark_transform',
        bash_command='spark-submit /opt/airflow/dags/../spark_jobs/transform_data.py'
    )

    transform
