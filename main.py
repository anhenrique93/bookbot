from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict
from stats import print_report
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print_report(path, num_words, num_chars)

main()