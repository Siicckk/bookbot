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

