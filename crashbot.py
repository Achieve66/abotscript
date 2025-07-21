def on_message(message):
    if message.content == "Are you bot?":
        # 模擬爆炸性錯誤格式 × 短內容
        bad_format = "<html>\n\n<h1>IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII</h1>\n\n</div>\n\n<markdown>*崩潰</markdown>"
        print(bad_format)
    else:
        print("HOPELESSSSSS")