from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    lower,
    regexp_replace,
    trim,
    split,
    expr
)
from pyspark.ml.feature import StopWordsRemover

# =====================================
# 1. KHỞI TẠO SPARK
# =====================================

spark = SparkSession.builder \
    .appName("TikTok_BigData_Preprocessing") \
    .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
    .getOrCreate()

print("[*] Khởi động Spark thành công")

# =====================================
# 2. ĐỌC FILE JSON
# =====================================

df = spark.read.option("multiline", "true").json([
    "video1_comments.json",
    "video2_comments.json",
    "video3_comments.json",
    "video4_comments.json",
    "video5_comments.json"
])

print(f"[+] Tổng số bình luận thô: {df.count()}")

# =====================================
# 3. CHỈ GIỮ CỘT CẦN THIẾT
# =====================================

df = df.select(
    "comment_id",
    "created_time",
    "text",
    "username",
    "likes"
)

# =====================================
# 4. XÓA DỮ LIỆU RỖNG
# =====================================

df = df.filter(col("text").isNotNull())
df = df.filter(trim(col("text")) != "")

print(f"[+] Sau khi xóa rỗng: {df.count()}")

# =====================================
# 5. XÓA DỮ LIỆU TRÙNG
# =====================================

df = df.dropDuplicates(["text", "username"])

print(f"[+] Sau khi xóa trùng: {df.count()}")

# =====================================
# 6. CHUYỂN CHỮ THƯỜNG
# =====================================

df = df.withColumn(
    "text",
    lower(col("text"))
)

# =====================================
# 7. XÓA URL
# =====================================

df = df.withColumn(
    "text",
    regexp_replace(
        col("text"),
        r"http\S+|www\S+",
        ""
    )
)

# =====================================
# 8. XÓA MENTION
# =====================================

df = df.withColumn(
    "text",
    regexp_replace(
        col("text"),
        r"@\w+",
        ""
    )
)

# =====================================
# 9. XÓA HASHTAG
# =====================================

df = df.withColumn(
    "text",
    regexp_replace(
        col("text"),
        r"#\w+",
        ""
    )
)

# =====================================
# 10. CHUẨN HÓA TEENCODE
# =====================================

teencode_dict = {
    "ko": "không",
    "kh": "không",
    "k": "không",
    "hk": "không",
    "dc": "được",
    "đc": "được",
    "mn": "mọi người",
    "mng": "mọi người",
    "rv": "review",
    "srm": "sữa rửa mặt",
    "mik": "mình",
    "mk": "mình",
    "dg": "đang",
    "z": "vậy",
    "r": "rồi",
    "e": "em",
    "t": "tôi"
}

for slang, standard in teencode_dict.items():
    df = df.withColumn(
        "text",
        regexp_replace(
            col("text"),
            f"\\b{slang}\\b",
            standard
        )
    )

# =====================================
# 11. XÓA KÝ TỰ ĐẶC BIỆT
# =====================================

df = df.withColumn(
    "text",
    regexp_replace(
        col("text"),
        r"[^a-zA-ZÀ-ỹ0-9\s]",
        " "
    )
)

# =====================================
# 12. CHUẨN HÓA KHOẢNG TRẮNG
# =====================================

df = df.withColumn(
    "text",
    trim(
        regexp_replace(
            col("text"),
            r"\s+",
            " "
        )
    )
)

# Xóa dòng rỗng sau tiền xử lý

df = df.filter(trim(col("text")) != "")

# =====================================
# 13. TOKENIZATION
# =====================================

df = df.withColumn(
    "words",
    split(col("text"), " ")
)

# =====================================
# 14. STOPWORDS
# =====================================

stopwords = [
    "là", "thì", "và", "ở", "của",
    "cho", "với", "này", "kia",
    "đó", "ấy", "nhưng", "mà",
    "đã", "đang", "sẽ", "có",
    "nha", "nhé", "ạ"
]

remover = StopWordsRemover(
    inputCol="words",
    outputCol="filtered_words",
    stopWords=stopwords
)

df = remover.transform(df)

# =====================================
# 15. XÓA TOKEN QUÁ NGẮN
# =====================================

df = df.withColumn(
    "filtered_words",
    expr(
        "filter(filtered_words, x -> length(x) > 1)"
    )
)

# =====================================
# 16. XEM KẾT QUẢ
# =====================================

print("\n===== 10 DÒNG SAU TIỀN XỬ LÝ =====")

df.select(
    "text",
    "filtered_words"
).show(10, truncate=False)

# =====================================
# 17. LƯU CSV
# =====================================

output_file = "BigData_Cleaned_Comments.csv"

df.toPandas().to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print(f"\n[+] Đã lưu thành công vào: {output_file}")

# =====================================
# 18. THỐNG KÊ
# =====================================

print(f"[+] Tổng số dòng cuối cùng: {df.count()}")

spark.stop()