from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NYC Taxi ETL") \
    .getOrCreate()

df = spark.read.parquet("s3a://nyc-taxi/yellow_tripdata_2023-01.parquet")

df_clean = df.selectExpr(
    "VendorID as vendor_id",
    "tpep_pickup_datetime as pickup_datetime",
    "tpep_dropoff_datetime as dropoff_datetime",
    "passenger_count",
    "trip_distance",
    "RatecodeID as rate_code",
    "payment_type",
    "total_amount"
).filter("passenger_count > 0 AND total_amount > 0")

df_clean.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/nyc") \
    .option("dbtable", "yellow_tripdata") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()
