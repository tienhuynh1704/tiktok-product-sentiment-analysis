from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, trim, split
from pyspark.ml.feature import StopWordsRemover

# 1. Khởi tạo
spark = SparkSession.builder \
    .appName("TikTok_BigData_Native") \
    .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
    .getOrCreate()

print("[*] Bắt đầu khởi động PySpark (Chế độ Native 100%)...")

# 2. Đọc file
df = spark.read.option("multiline", "true").json("video*_comments.json")
print(f"[+] Đã gộp thành công! Tổng số bình luận thô: {df.count()} dòng")

# 3. Lọc rỗng và trùng
df_clean = df.filter(col("text").isNotNull()).dropDuplicates(["text", "username"])
print(f"[-] Dữ liệu sạch sau khi lọc: {df_clean.count()} dòng")

# 4. Chữ thường và Xóa ký tự đặc biệt
df_clean = df_clean.withColumn("text", lower(col("text")))
df_clean = df_clean.withColumn("text", regexp_replace(col("text"), r"[^\w\s]", ""))

# 5. Dịch Teencode cơ bản bằng Lõi Native (Tuyệt đối không dùng UDF)
teencode_dict = {
    "sp": "sản phẩm", "ko": "không", "k": "không", "dc": "được", "đc": "được",
    "mik": "mình", "mk": "mình", "srm": "sữa rửa mặt", "lun": "luôn"
}
for slang, standard in teencode_dict.items():
    df_clean = df_clean.withColumn("text", regexp_replace(col("text"), f"\\b{slang}\\b", standard))

df_clean = df_clean.withColumn("text", trim(regexp_replace(col("text"), " +", " ")))

# 6. Tách từ siêu tốc
df_tokenized = df_clean.withColumn("words", split(col("text"), " "))

# 7. Xóa Stopwords
vietnamese_stopwords = ["là", "thì", "và", "ở", "của", "nè", "ạ", "nhé", "nha", "để", "có", "cho", "với", "nhưng", "mà", "đã", "đang", "sẽ", "những", "các", "này", "kia", "đó", "đây", "ấy", "nào", "cái", "con", "chiếc"]
remover = StopWordsRemover(inputCol="words", outputCol="filtered_words", stopWords=vietnamese_stopwords)
df_final = remover.transform(df_tokenized)

# 8. Nghiệm thu và Xuất file
print("\n--- 10 BÌNH LUẬN ĐÃ ĐƯỢC LÀM SẠCH ---")
df_final.select("username", "filtered_words").show(10, truncate=False)

output_folder = "BigData_Cleaned_Comments.parquet"
df_final.write.mode("overwrite").parquet(output_folder)
print(f"\n[+] HOÀN TẤT XUẤT SẮC! Dữ liệu đã an toàn trong: {output_folder}")