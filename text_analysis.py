import re
from collections import Counter

# -------------------------------
# TEXT ANALYSIS SYSTEM
# -------------------------------

# Common stop words
STOP_WORDS = {
    "the", "is", "a", "an", "and", "or", "of", "to", "in",
    "on", "for", "with", "this", "that", "it", "as", "are",
    "was", "were", "be", "by", "from", "at", "has", "have",
    "had", "will", "can", "about", "very", "more", "but",
    "their", "they", "we", "you", "he", "she", "i"
}

# Simple sentiment dictionary
POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "useful",
    "helpful", "happy", "love", "best", "positive",
    "successful", "effective", "safe", "clean", "beautiful"
}

NEGATIVE_WORDS = {
    "bad", "poor", "terrible", "worst", "hate", "negative",
    "problem", "danger", "dangerous", "pollution", "dirty",
    "harmful", "failure", "difficult", "waste"
}


def analyze_text(text):

    # -------------------------------
    # 1. Convert text to lowercase
    # -------------------------------
    clean_text = text.lower()

    # -------------------------------
    # 2. Extract words
    # -------------------------------
    words = re.findall(r'\b[a-zA-Z]+\b', clean_text)

    # -------------------------------
    # 3. Remove stop words
    # -------------------------------
    meaningful_words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    # -------------------------------
    # 4. Word frequency
    # -------------------------------
    frequency = Counter(meaningful_words)

    # -------------------------------
    # 5. Sentence analysis
    # -------------------------------
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    # -------------------------------
    # 6. Sentiment analysis
    # -------------------------------
    positive = [
        word for word in words
        if word in POSITIVE_WORDS
    ]

    negative = [
        word for word in words
        if word in NEGATIVE_WORDS
    ]

    if len(positive) > len(negative):
        sentiment = "Positive"
    elif len(negative) > len(positive):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # -------------------------------
    # 7. Readability calculation
    # -------------------------------
    word_count = len(words)
    sentence_count = len(sentences)

    if sentence_count > 0:
        average_sentence_length = word_count / sentence_count
    else:
        average_sentence_length = 0

    # -------------------------------
    # 8. Display results
    # -------------------------------
    print("\n" + "=" * 50)
    print("           TEXT ANALYSIS REPORT")
    print("=" * 50)

    print("\nBasic Statistics")
    print("-" * 30)
    print("Total words        :", word_count)
    print("Unique words       :", len(set(words)))
    print("Total sentences    :", sentence_count)
    print("Average sentence   :", round(average_sentence_length, 2),
          "words")

    print("\nSentiment Analysis")
    print("-" * 30)
    print("Sentiment           :", sentiment)
    print("Positive words      :", len(positive))
    print("Negative words      :", len(negative))

    print("\nKeywords / Frequent Words")
    print("-" * 30)

    for word, count in frequency.most_common(10):
        print(f"{word:<20} {count}")

    print("\nDetected Positive Words")
    print("-" * 30)
    print(", ".join(set(positive)) if positive else "None")

    print("\nDetected Negative Words")
    print("-" * 30)
    print(", ".join(set(negative)) if negative else "None")

    print("\n" + "=" * 50)


# -------------------------------
# MAIN PROGRAM
# -------------------------------

print("TEXT ANALYSIS SYSTEM")
print("=" * 50)

text = input("\nEnter the text to analyze:\n")

if text.strip():
    analyze_text(text)
else:
    print("Please enter some text.")