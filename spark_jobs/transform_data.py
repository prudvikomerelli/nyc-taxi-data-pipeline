from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
import os

spark = SparkSession.builder \
    .appName("NYC Taxi Transform") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

df = spark.read.option("header", "true").csv("s3a://nyc-data/yellow_tripdata_sample.csv")

df = df.withColumn("tpep_pickup_datetime", to_timestamp("tpep_pickup_datetime")) \
       .withColumn("tpep_dropoff_datetime", to_timestamp("tpep_dropoff_datetime")) \
       .filter(col("passenger_count") > 0)

df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/taxi_data") \
    .option("dbtable", "trips") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .mode("overwrite") \
    .save()

spark.stop()
