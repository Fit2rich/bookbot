def get_boot_text(filepath):
    with open(filepath,'r' ) as f:
        text = f.read()
    return text


def count_words(text):
    words = text.split()
    num_words  = len(words)
    return num_words



def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_boot_text(filepath)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")





if __name__ == '__main__':
  main()