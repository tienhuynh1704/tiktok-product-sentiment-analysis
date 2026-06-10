# TikTok Product Sentiment Analysis

## Introduction

This project analyzes user sentiment from TikTok product review comments using Big Data technologies and Machine Learning.

## Technologies

* Python
* PySpark
* Pandas
* Scikit-learn
* TF-IDF
* Logistic Regression
* TikTokLive API

## Project Workflow

### 1. Data Collection

* Crawl comments from TikTok videos
* Store data in JSON and CSV formats

### 2. Data Preprocessing

* Remove duplicates
* Remove URLs, hashtags, mentions
* Normalize teencode
* Tokenization
* Stopword removal

### 3. Exploratory Data Analysis (EDA)

* Word Frequency Analysis
* Word Cloud Visualization
* Sentiment Distribution

### 4. Sentiment Labeling

* Rule-based sentiment labeling

### 5. Model Training

* TF-IDF Vectorization
* Logistic Regression Classification

### 6. Model Evaluation

* Accuracy: 92.53%

### 7. Real-time Prediction

* Predict sentiment from user comments
* Support TikTok livestream comment monitoring

## How to Run

```bash
python preprocessing_final_v2.py
python label_sentiment.py
python train_model.py
python evaluate_model.py
python predict_realtime.py
```

## Author

Tien Huynh
