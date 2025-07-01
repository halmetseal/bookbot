from stats import *
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    argv = sys.argv

    if len(argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = argv[1]
    book_text = get_book_text(path)
    word_count = get_word_count(book_text)
    char_counts = sort_by_char_count(get_character_count(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for k in char_counts:
        if k["char"].isalpha():
            print(f"{k["char"]}: {k["num"]}")
    print("============= END ===============")


main()
