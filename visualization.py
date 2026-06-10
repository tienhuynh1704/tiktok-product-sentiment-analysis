import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sentiment_Labeled.csv")

counts = df["sentiment"].value_counts()

plt.figure(figsize=(8,5))
counts.plot(kind="bar")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("Sentiment_Distribution.png")

print("Đã lưu Sentiment_Distribution.png")