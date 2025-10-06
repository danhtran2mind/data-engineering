# Services Setup

## Installation

### Hadoop/HDFS

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzvf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /opt/hadoop
# Add Hadoop bin to PATH in ~/.bashrc or ~/.zshrc:
export HADOOP_HOME=/opt/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```
> Configure core-site.xml and hdfs-site.xml as needed for your environment.

### Spark

```bash
wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar -xzvf spark-3.5.1-bin-hadoop3.tgz
sudo mv spark-3.5.1-bin-hadoop3 /opt/spark
# Add Spark bin to PATH in ~/.bashrc or ~/.zshrc:
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin
```

### Airflow

```bash
pip install apache-airflow
# Initialize Airflow DB and create default user:
airflow db init
```

> For more details, see the official docs for [Hadoop](https://hadoop.apache.org/), [Spark](https://spark.apache.org/), and [Airflow](https://airflow.apache.org/).

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
