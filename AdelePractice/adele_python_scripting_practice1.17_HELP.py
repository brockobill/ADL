import re
from collections import Counter

def CommonWord(string):
    # Tokenize the input text into words (excluding special characters)
    words = re.findall(r'\b[^\W\d_]+\b', string.lower())

    # Count the occurrences of each word
    word_counts = Counter(words)

    if not word_counts:
        return 0  # Return 0 if there are no words

    # Find the most frequently occurring word count
    most_frequent_count = max(word_counts.values())
    return most_frequent_count

# Test case
result = CommonWord("black dog, brown dog, white dog")
print(result)
