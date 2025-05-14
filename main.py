from stats import num_words 
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = num_words(book_text)
    print(f"{count} words found in the document")
main()    
