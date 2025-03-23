def get_num_words(text):
    words_list = text.split()
    return len(words_list)


def get_chars_dict(text):
    text_lower = text.lower()
    chars_dict = {}
    for char in text_lower:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict