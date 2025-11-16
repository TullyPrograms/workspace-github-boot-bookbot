import sys
from reader import get_book_text
from stats import word_count, get_character_num, sort_char

if (len(sys.argv)) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    char_counts = get_character_num(text)
    sorted_chars = sort_char(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()