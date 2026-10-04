def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        text = file.read()

    punctuation = ".,!?;:()[]'\""

    for mark in punctuation:
        text = text.replace(mark, "")

    words = text.split()

    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return {word: count for word, count in counts.items() if count >= lower_limit}