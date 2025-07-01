from stats import *


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    char_counts = get_character_count(book_text)
    print(f"{word_count} words found in the document")
    print(char_counts)


main()
