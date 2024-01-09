def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    print(f"There are {count} words in the book.")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words_list = text.split()
    return len(words_list)


main()