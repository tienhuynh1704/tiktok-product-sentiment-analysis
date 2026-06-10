from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent

# ==================================
# USERNAME TIKTOK ĐANG LIVESTREAM
# (KHÔNG có @)
# ==================================

USERNAME = "hadalabo_vietnam"

# ==================================
# TẠO CLIENT
# ==================================

client = TikTokLiveClient(
    unique_id=USERNAME
)

# ==================================
# KHI KẾT NỐI THÀNH CÔNG
# ==================================

@client.on(ConnectEvent)
async def on_connect(event):

    print("\n==============================")
    print("KẾT NỐI LIVESTREAM THÀNH CÔNG")
    print("Room ID:", client.room_id)
    print("==============================\n")


# ==================================
# NHẬN COMMENT REALTIME
# ==================================

@client.on(CommentEvent)
async def on_comment(event):

    print(
        f"{event.user.nickname}: "
        f"{event.comment}"
    )


# ==================================
# CHẠY CHƯƠNG TRÌNH
# ==================================

if __name__ == "__main__":

    print(
        f"Đang kết nối livestream TikTok của: {USERNAME}"
    )

    try:

        client.run()

    except Exception as e:

        print("\n[LỖI KẾT NỐI]")
        print(e)

        print(
            "\nKiểm tra lại:"
        )

        print(
            "- Username có đúng không?"
        )

        print(
            "- Kênh có đang livestream không?"
        )

        print(
            "- Username KHÔNG có ký tự @"
        )