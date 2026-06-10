import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu đã gán nhãn
df = pd.read_csv("Sentiment_Labeled.csv")

# Thống kê số lượng từng nhãn
counts = df["sentiment"].value_counts()

print("\n===== PHÂN BỐ NHÃN CẢM XÚC =====")
print(counts)

# Vẽ biểu đồ
plt.figure(figsize=(8, 5))

counts.plot(
    kind="bar"
)

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Comments")

plt.tight_layout()

plt.savefig(
    "Sentiment_Distribution.png"
)

print("\nĐã lưu Sentiment_Distribution.png")
