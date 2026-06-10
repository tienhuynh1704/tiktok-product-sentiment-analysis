import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================
# Đọc dữ liệu
# ==========================

df = pd.read_csv("Sentiment_Labeled.csv")

df = df.dropna(subset=["text", "sentiment"])

print("Tổng dữ liệu:", len(df))

# ==========================
# X và y
# ==========================

X = df["text"]
y = df["sentiment"]

# ==========================
# Train Test Split
# ==========================

X_train_text, X_test_text, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Train:", len(X_train_text))
print("Test :", len(X_test_text))

# ==========================
# TF-IDF
# ==========================

tfidf = TfidfVectorizer(
    max_features=5000,
    min_df=3,
    max_df=0.9,
    ngram_range=(1, 2)
)

X_train = tfidf.fit_transform(X_train_text)
X_test = tfidf.transform(X_test_text)

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

print("\nAccuracy =", round(acc * 100, 2), "%")

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

print("\nModel saved successfully!")