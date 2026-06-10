from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

spark = SparkSession.builder \
    .appName("TikTok") \
    .getOrCreate()

df = spark.read.csv(
    "Sentiment_Labeled.csv",
    header=True,
    inferSchema=True
)

result = df.groupBy("sentiment").count().toPandas()

plt.figure(figsize=(6,4))
plt.bar(result["sentiment"], result["count"])

plt.title("Sentiment Distribution Using Spark")
plt.savefig("Spark_Sentiment_Distribution.png")

spark.stop()
