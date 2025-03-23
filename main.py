from stats import get_num_words, get_chars_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_dict):
    # Convert chars_dict to a list of tuples and 
    # sort in descending order by char count
    chars_list = sorted(chars_dict.items(), key=lambda char: char[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("\n")
    for char in chars_list:
        if char[0].isalpha():
            print(f"'{char[0]}': {char[1]}")
    print("--- End report ---")


main()