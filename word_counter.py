def count_words_and_characters(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    return num_words, num_chars

if __name__ == "__main__":
    sample_text = "This is a test sentence."
    words, chars = count_words_and_characters(sample_text)
    print("Words:", words)
    print("Characters:", chars)
