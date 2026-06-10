import pandas as pd

# ==========================
# Đọc dữ liệu đã xử lý
# ==========================

df = pd.read_csv(
    "BigData_Cleaned_Comments.csv",
    encoding="utf-8-sig"
)

# ==========================
# Từ điển cảm xúc
# ==========================

positive_words = [
    "tốt",
    "đẹp",
    "xịn",
    "thích",
    "ok",
    "ổn",
    "hay",
    "tuyệt",
    "đỉnh",
    "hợp",
    "mượt",
    "sạch",
    "yêu",
    "chất",
    "mê",
    "ưng",
    "hiệu quả",
    "đáng tiền"
]

negative_words = [
    "tệ",
    "dở",
    "chán",
    "xấu",
    "kém",
    "ngứa",
    "rát",
    "mụn",
    "khô",
    "không hợp",
    "thất vọng",
    "đắt",
    "dị ứng",
    "hôi",
    "lừa",
    "fake"
]

# ==========================
# Hàm gán nhãn
# ==========================

def sentiment_label(text):

    text = str(text).lower()

    pos = 0
    neg = 0

    for word in positive_words:
        if word in text:
            pos += 1

    for word in negative_words:
        if word in text:
            neg += 1

    if pos > neg:
        return "Positive"

    elif neg > pos:
        return "Negative"

    else:
        return "Neutral"

# ==========================
# Gán nhãn
# ==========================

df["sentiment"] = df["text"].apply(
    sentiment_label
)

# ==========================
# Lưu file
# ==========================

df.to_csv(
    "Sentiment_Labeled.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Đã tạo Sentiment_Labeled.csv")

print(
    df["sentiment"]
    .value_counts()
)