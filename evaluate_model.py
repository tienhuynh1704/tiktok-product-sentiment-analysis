import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

df = pd.read_csv("Sentiment_Labeled.csv")

df = df.dropna(subset=["text", "sentiment"])

X = df["text"]
y = df["sentiment"]

X_train_text, X_test_text, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

vectorizer = joblib.load(
    "tfidf_vectorizer.pkl"
)

model = joblib.load(
    "sentiment_model.pkl"
)

X_test = vectorizer.transform(
    X_test_text
)

y_pred = model.predict(
    X_test
)

print("\nAccuracy:")
print(
    accuracy_score(
        y_test,
        y_pred
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)