from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TikTok_Test") \
    .getOrCreate()

print("SPARK OK")

spark.stop()