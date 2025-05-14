from stats import num_words
from stats import num_character
from stats import sorted_chars_list
import sys 
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    count = num_words(book_text)
    print(f"Found {count} total words")
    char_count = num_character(book_text)
    sorted_chars = sorted_chars_list(char_count)
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        char = char_info["char"]
        if char.isalpha():
            num = char_info["num"]
            print(f"{char}: {num}")
    print("============= END ===============")
main()    
