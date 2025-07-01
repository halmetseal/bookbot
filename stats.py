def get_word_count(str):
    return len(str.split())


def get_character_count(str):
    char_counts = {}
    for c in str:
        c = c.lower()
        char_counts[c] = char_counts.get(c, 0) + 1
    return char_counts
