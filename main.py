from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    text_lower = text.lower()
    chars_dict = {}
    for char in text_lower:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def print_report(book_path, num_words, chars_dict):
    # Convert chars_dict to a list of tuples and 
    # sort in descending order by char count
    chars_list = sorted(chars_dict.items(), key=lambda char: char[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} words found in the document.")
    print("\n")
    for char in chars_list:
        if char[0].isalpha():
            print(f'The "{char[0]}" character was found {char[1]} times.')
    print("--- End report ---")


main()