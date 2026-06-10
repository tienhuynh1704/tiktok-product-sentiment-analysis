import pandas as pd
import json

# Đọc file json đã cào được
with open('tiktok_comments.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Chuyển thành DataFrame (Bảng)
df = pd.DataFrame(data)

# Chỉ chọn các cột thông tin quan trọng để lưu vào CSV
# (Bỏ cột ảnh đi cho file nó sạch và không lỗi Excel nữa)
cols_to_keep = ['id', 'comment_id', 'created_time', 'text', 'username', 'nickname', 'likes', 'replies']
df_clean = df[cols_to_keep]

# Lưu thành file CSV (Định dạng utf-8-sig để Excel không bị lỗi font tiếng Việt)
df_clean.to_csv('tiktok_comments_clean.csv', index=False, encoding='utf-8-sig')

print("Đã tạo file 'tiktok_comments_clean.csv' thành công!")
print("Hãy mở file này bằng Excel, đảm bảo không bao giờ bị lỗi nữa!")