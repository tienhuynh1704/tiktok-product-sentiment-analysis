import os
import joblib

from TikTokLive import TikTokLiveClient
from TikTokLive.events import (
    ConnectEvent,
    CommentEvent
)

# =====================================
# KIỂM TRA MODEL
# =====================================

MODEL_FILE = "sentiment_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"

if not os.path.exists(MODEL_FILE):
    print(f"[LỖI] Không tìm thấy: {MODEL_FILE}")
    print("Hãy chạy:")
    print("python train_model.py")
    exit()

if not os.path.exists(VECTORIZER_FILE):
    print(f"[LỖI] Không tìm thấy: {VECTORIZER_FILE}")
    print("Hãy chạy:")
    print("python train_model.py")
    exit()

# =====================================
# LOAD MODEL
# =====================================

print("[*] Đang load model...")

model = joblib.load(
    MODEL_FILE
)

vectorizer = joblib.load(
    VECTORIZER_FILE
)

print("[+] Load model thành công!")

# =====================================
# USERNAME LIVESTREAM
# KHÔNG CÓ @
# =====================================

USERNAME = "hadalabo_vietnam"

# Ví dụ:
# USERNAME = "mint_cosmetics"
# USERNAME = "thegioiskinfood"

# =====================================
# TẠO CLIENT
# =====================================

client = TikTokLiveClient(
    unique_id=USERNAME
)

# =====================================
# KẾT NỐI THÀNH CÔNG
# =====================================

@client.on(ConnectEvent)
async def on_connect(event):

    print("\n==============================")
    print("KẾT NỐI LIVESTREAM THÀNH CÔNG")
    print("TikTok:", USERNAME)
    print("Room ID:", client.room_id)
    print("==============================\n")


# =====================================
# COMMENT REALTIME + PREDICT
# =====================================

@client.on(CommentEvent)
async def on_comment(event):

    try:

        comment = event.comment

        vec = vectorizer.transform(
            [comment]
        )

        pred = model.predict(
            vec
        )[0]

        print("\n========================")
        print("USER      :", event.user.nickname)
        print("COMMENT   :", comment)
        print("SENTIMENT :", pred)
        print("========================")

    except Exception as e:

        print(
            f"[LỖI DỰ ĐOÁN] {e}"
        )


# =====================================
# RUN
# =====================================

if __name__ == "__main__":

    print(
        f"\n[*] Đang kết nối livestream TikTok của: {USERNAME}"
    )

    try:

        client.run()

    except Exception as e:

        print("\n[LỖI KẾT NỐI]")
        print(e)

        print("\nKiểm tra:")
        print("- Username đúng chưa?")
        print("- Kênh có đang livestream không?")
        print("- Username không có @")