import joblib

MODEL_FILE = "sentiment_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"

model = joblib.load(
    MODEL_FILE
)

vectorizer = joblib.load(
    VECTORIZER_FILE
)

print("Model loaded!")

while True:

    comment = input(
        "\nNhập comment (exit để thoát): "
    )

    if comment.lower() == "exit":
        break

    vec = vectorizer.transform(
        [comment]
    )

    pred = model.predict(
        vec
    )

    print(
        "Sentiment:",
        pred[0]
    )