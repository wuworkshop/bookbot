def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = get_letters_dict(text)
    print(letters_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words_list = text.split()
    return len(words_list)


def get_letters_dict(text):
    text_lower = text.lower()
    letters_dict = {}
    for letter in text_lower:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

main()