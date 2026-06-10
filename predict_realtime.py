while True:
    comment = input("Nhập comment (exit để thoát): ")

    if comment.lower() == "exit":
        break

    vec = vectorizer.transform([comment])
    pred = model.predict(vec)

    print("Sentiment:", pred[0])