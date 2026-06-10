import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import joblib

# ==========================
# Đọc dữ liệu
# ==========================

df = pd.read_csv("Sentiment_Labeled.csv")

df = df.dropna()

print("Tổng dữ liệu:", len(df))

# ==========================
# X
# ==========================

X = df["text"]

# ==========================
# y
# ==========================

y = df["sentiment"]

# ==========================
# TF-IDF
# ==========================

tfidf = TfidfVectorizer(
    max_features=5000,
    min_df=3,
    max_df=0.9,
    ngram_range=(1,2)
)

X_tfidf = tfidf.fit_transform(X)

# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf,
    y,
    test_size=0.2,
    random_state=42
)

print("Train:", X_train.shape)
print("Test :", X_test.shape)

# ==========================
# Logistic Regression
# ==========================

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

# ==========================
# Predict
# ==========================

y_pred = model.predict(X_test)

# ==========================
# Accuracy
# ==========================

acc = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy =", round(acc*100,2), "%")

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred
    )
)

print("\nConfusion Matrix:\n")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

# ==========================
# Save model
# ==========================

joblib.dump(
    model,
    "sentiment_model.pkl"
)

joblib.dump(
    tfidf,
    "tfidf_vectorizer.pkl"
)

print("\nModel saved.")