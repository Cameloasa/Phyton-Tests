def count_words(sentence: str) -> int:
    words = sentence
    if words == "" or words == "  ":
        return 0
    return len(words)