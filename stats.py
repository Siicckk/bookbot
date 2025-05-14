def num_words(book_text):
    words = book_text.split()
    return len(words)
def num_character(book_text):
    word_count = {}
    lower_case = book_text.lower()
    for char in lower_case:
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    return word_count
def sorted_chars_list(char_dict):
    def sort_on(dict_item):
        return dict_item["num"]

    result_list = []

    for char, count in char_dict.items():
        char_info = {"char": char, "num": count}
        result_list.append(char_info)

    result_list.sort(reverse=True, key=sort_on)
    return result_list
