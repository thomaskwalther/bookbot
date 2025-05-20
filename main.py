import sys
import string
from stats import get_book_text, count_the_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    wc, fc = get_book_text(path)
    dict_word = count_the_characters(fc)
    alphanumeric = set(string.ascii_lowercase + string.digits)
    filtered_list = [
        {"letter": k, "num": v}
        for k, v in dict_word.items() if k in alphanumeric
    ]
    filtered_list.sort(key=lambda x: x["num"], reverse=True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in filtered_list:
        print(f"{item['letter']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()