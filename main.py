from stats import get_word_count, get_char_freq, sort_freqs
import sys

def main():
    path = None
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
        
    contents = get_book_text(path)
    words_count = get_word_count(contents)
    char_freq = get_char_freq(contents)
    sorted_freqs = sort_freqs(char_freq)
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}...".format(path=path))
    print("----------- Word Count ----------")
    print("Found {count} total words".format(count=words_count))
    print("--------- Character Count -------")
    for entry in sorted_freqs:
        char = entry["char"]
        count = entry["count"]
        p = "{char}: {count}".format(char=char, count=count)
        if char.isalpha():
            print(p)
    print("============= END ===============")


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        contents = f.read()
        return contents



main()