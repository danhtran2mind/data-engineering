# Services Setup

## Airflow

Start the Airflow webserver and scheduler:

```bash
airflow db init
airflow webserver -p 8080 &
airflow scheduler &
```

Access Airflow UI at: [http://localhost:8080](http://localhost:8080)

## Hadoop/HDFS

Start Hadoop services (namenode, datanode):

```bash
start-dfs.sh
```

Check HDFS status:

```bash
hdfs dfsadmin -report
```

## Spark

No separate service needed; Spark jobs are run via `spark-submit` from the Airflow DAG or manually.

## TensorFlow/Keras

Python dependencies are required for LSTM training and prediction. See [dependencies.md](dependencies.md).

## Troubleshooting

- If Airflow or Hadoop services fail to start, check logs for port conflicts or missing configuration.
- Ensure `$PATH` includes Hadoop, Spark, and Airflow binaries.
