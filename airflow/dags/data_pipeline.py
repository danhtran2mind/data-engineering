from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 1),
}

with DAG('data_engineering_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    # 1. Download Binance BTCUSDT 1s kline CSV (example: 2024-05)
    download_csv = BashOperator(
        task_id='download_csv',
        bash_command='wget -O /tmp/BTCUSDT-1s-2024-05.csv "https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1s/BTCUSDT-1s-2024-05.csv.gz" && gunzip -f /tmp/BTCUSDT-1s-2024-05.csv.gz'
    )

    # 2. Move data to HDFS
    move_to_hdfs = BashOperator(
        task_id='move_to_hdfs',
        bash_command='hdfs dfs -put -f /tmp/BTCUSDT-1s-2024-05.csv /data/raw/'
    )

    # 3. Spark job to process data (optional, e.g., cleaning)
    process_data = BashOperator(
        task_id='process_data',
        bash_command='spark-submit /workspaces/data-engineering/spark/process_data.py'
    )

    # 4. LSTM deep learning training
    lstm_train = BashOperator(
        task_id='lstm_train',
        bash_command='python3 /workspaces/data-engineering/spark/lstm_train.py'
    )

    # 5. LSTM deep learning prediction
    lstm_predict = BashOperator(
        task_id='lstm_predict',
        bash_command='python3 /workspaces/data-engineering/spark/lstm_predict.py'
    )

    download_csv >> move_to_hdfs >> process_data >> lstm_train >> lstm_predict
    export_mongodb = BashOperator(
        task_id='export_mongodb',
        bash_command='mongoexport --uri="$MONGODB_URI" --collection=blog_posts --out=/tmp/blog_posts.json'
    )

    # 6. Move all data to HDFS
    move_to_hdfs = BashOperator(
        task_id='move_to_hdfs',
        bash_command="""
        hdfs dfs -put -f /tmp/gtd_sample.csv /data/raw/
        hdfs dfs -put -f /tmp/crypto_prices.json /data/raw/
        hdfs dfs -put -f /tmp/customer_orders.csv /data/raw/
        hdfs dfs -put -f /tmp/blog_posts.json /data/raw/
        """
    )

    # 7. Spark job to process data
    process_data = BashOperator(
        task_id='process_data',
        bash_command='spark-submit /workspaces/data-engineering/spark/process_data.py'
    )

    download_csv >> fetch_api >> export_supabase >> export_mongodb >> move_to_hdfs >> process_data
    download_csv >> fetch_api >> export_supabase >> export_mongodb >> move_to_hdfs >> process_data
