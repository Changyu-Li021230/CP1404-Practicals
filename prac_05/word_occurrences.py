"""Word Occurrences：
Estimate: 15 minutes
Actual: 13 minutes

This program asks the user to enter a line of text,
counts how many times each word appears,
and displays the results sorted alphabetically
with aligned formatting based on the longest word.
"""

def main():
    """Get text input, count words, and display sorted results."""
    text = get_text()
    word_to_count = count_words(text)
    display_counts(word_to_count)


def get_text() -> str:
    """Get a line of text from the user and return it."""
    return input("Text: ").strip()


def count_words(text: str) -> dict[str, int]:
    """Return a dictionary mapping each word to its count."""
    word_to_count: dict[str, int] = {}
    words = text.split()
    for word in words:
        # Use EAFP (Easier to Ask Forgiveness than Permission)
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def display_counts(word_to_count: dict[str, int]) -> None:
    """Display each word and its count, sorted alphabetically and aligned."""
    sorted_words = sorted(word_to_count)
    max_word_length = max(len(word) for word in sorted_words)
    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()
