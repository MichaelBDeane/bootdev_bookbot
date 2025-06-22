from stats import get_word_count
from stats import character_count
from stats import character_sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = character_count(text)
    char_sorted_list = character_sort(char_count)
    print_report(book_path, word_count, char_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, count, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()