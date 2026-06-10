import pandas as pd
import ast

from collections import Counter
from nltk import ngrams

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# =====================================
# ĐỌC FILE
# =====================================

df = pd.read_csv(
    "BigData_Cleaned_Comments.csv",
    encoding="utf-8-sig"
)

print("Tổng số comment:", len(df))

# =====================================
# 4.3.1 TEXT LENGTH ANALYSIS
# =====================================

def count_words(text):

    try:
        words = ast.literal_eval(text)

        return len(words)

    except:

        return 0

df["word_count"] = df["filtered_words"].apply(
    count_words
)

print("\n===== THỐNG KÊ ĐỘ DÀI =====")

print(
    "Số từ trung bình:",
    round(df["word_count"].mean(),2)
)

print(
    "Số từ lớn nhất:",
    df["word_count"].max()
)

print(
    "Số từ nhỏ nhất:",
    df["word_count"].min()
)

# =====================================
# 4.3.2 UNIGRAM
# =====================================

all_words = []

for row in df["filtered_words"]:

    try:

        words = ast.literal_eval(row)

        all_words.extend(words)

    except:
        pass

counter = Counter(all_words)

top20 = counter.most_common(20)

print("\n===== TOP 20 WORDS =====")

for word, freq in top20:

    print(word, freq)

# =====================================
# BAR CHART
# =====================================

words = [x[0] for x in top20]

freqs = [x[1] for x in top20]

plt.figure(figsize=(12,6))

plt.bar(words, freqs)

plt.xticks(rotation=45)

plt.title("Top 20 Most Frequent Words")

plt.tight_layout()

plt.savefig(
    "Top20_Words.png"
)

print(
    "\nĐã lưu Top20_Words.png"
)

# =====================================
# BIGRAM
# =====================================

bigrams = []

for row in df["filtered_words"]:

    try:

        words = ast.literal_eval(row)

        bigrams.extend(
            list(
                ngrams(words,2)
            )
        )

    except:
        pass

bigram_counter = Counter(bigrams)

print("\n===== TOP 20 BIGRAM =====")

for pair, freq in bigram_counter.most_common(20):

    print(
        " ".join(pair),
        freq
    )

# =====================================
# WORD CLOUD
# =====================================

wc = WordCloud(
    width=1200,
    height=600,
    background_color="white"
)

wc.generate_from_frequencies(
    counter
)

plt.figure(figsize=(14,7))

plt.imshow(wc)

plt.axis("off")

plt.tight_layout()

plt.savefig(
    "WordCloud.png"
)

print(
    "\nĐã lưu WordCloud.png"
)