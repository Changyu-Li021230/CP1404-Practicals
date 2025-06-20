"""
Word Occurrences
Estimate: 15 minutes
Actual:   13 minutes

This program prompts the user to enter a line of text,
then counts how many times each word appears in the input.
It displays the results sorted alphabetically,
with aligned formatting based on the longest word.
"""

def main():
    """Count and display sorted, aligned word occurrences from user input."""
    word_to_count = {}
    text = input("Text: ")
    words = text.split()

    # Count each word using EAFP dictionary get method
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Get sorted list of unique words
    sorted_words = sorted(word_to_count)

    # Determine width for alignment
    max_word_length = max(len(word) for word in sorted_words)

    # Display results with formatting
    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()
