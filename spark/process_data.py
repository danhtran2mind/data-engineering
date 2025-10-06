from pyspark.sql import SparkSession
import duckdb

spark = SparkSession.builder.appName("DataEngineeringProcess").getOrCreate()

# Load datasets from HDFS
taxi_df = spark.read.csv("hdfs:///data/raw/nyc_taxi.csv", header=True, inferSchema=True)
weather_df = spark.read.json("hdfs:///data/raw/weather.json")
user_activity_df = spark.read.csv("hdfs:///data/raw/user_activity.csv", header=True, inferSchema=True)
transactions_df = spark.read.json("hdfs:///data/raw/transactions.json")

# Example transformation: count taxi trips per day
taxi_daily = taxi_df.groupBy("tpep_pickup_datetime").count()

# Save processed data to HDFS
taxi_daily.write.mode("overwrite").parquet("hdfs:///data/processed/taxi_daily.parquet")

# Save to DuckDB for analytics
taxi_daily_pd = taxi_daily.toPandas()
con = duckdb.connect("/workspaces/data-engineering/analytics/data.duckdb")
con.execute("CREATE TABLE IF NOT EXISTS taxi_daily AS SELECT * FROM taxi_daily_pd")
con.close()
