from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TikTok Sentiment Analysis") \
    .getOrCreate()

df = spark.read.csv(
    "Sentiment_Labeled.csv",
    header=True,
    inferSchema=True
)

print("Tong so comment:")
print(df.count())

print("Phan bo cam xuc:")
df.groupBy("sentiment").count().show()

spark.stop()