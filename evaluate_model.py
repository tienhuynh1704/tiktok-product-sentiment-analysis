import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load data
df = pd.read_csv("Sentiment_Labeled.csv")

df = df.dropna(subset=["text", "sentiment"])

X_text = df["text"]
y = df["sentiment"]

# Load vectorizer
vectorizer = joblib.load("tfidf_vectorizer.pkl")

X = vectorizer.transform(X_text)

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Load model
model = joblib.load("sentiment_model.pkl")

# Predict
y_pred = model.predict(X_test)

print("Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))