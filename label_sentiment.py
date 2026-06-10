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
    "đáng tiền",
    "rẻ",
    "ngon",
    "5 sao"
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
    "fake",
    "1 sao",
    "lỗi"
]

# ==========================
# Hàm gán nhãn
# ==========================

def sentiment_label(text):

    text = str(text).lower()

    # Xử lý phủ định
    negative_patterns = [
        "không tốt",
        "không đẹp",
        "không ổn",
        "không thích",
        "không hợp",
        "không hiệu quả",
        "không đáng tiền",
        "chẳng tốt",
        "chẳng đẹp",
        "chẳng thích"
    ]

    positive_patterns = [
        "không tệ",
        "không xấu",
        "không chán"
    ]

    for pattern in positive_patterns:
        if pattern in text:
            return "Positive"

    for pattern in negative_patterns:
        if pattern in text:
            return "Negative"

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
# Thống kê
# ==========================

print("\n===== PHÂN BỐ NHÃN =====")

print(
    df["sentiment"].value_counts()
)

# ==========================
# Lưu file
# ==========================

df.to_csv(
    "Sentiment_Labeled.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nĐã tạo Sentiment_Labeled.csv thành công!")