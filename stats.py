def get_word_count(str):
    return len(str.split())


def get_character_count(str):
    char_counts = {}
    for c in str:
        c = c.lower()
        char_counts[c] = char_counts.get(c, 0) + 1
    return char_counts


def sort_on(char_dict):
    return char_dict["num"]


def sort_by_char_count(chars):
    sorted_dicts = []
    for k in chars:
        sorted_dicts.append({"char": k, "num": chars[k]})
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts
