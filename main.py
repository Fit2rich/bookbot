import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list


def get_book_text(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text


def main():
   
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():  # Only print letters
            print(f"{char}: {item['num']}")

    print("============= END ===============")


if __name__ == '__main__':
    main()
