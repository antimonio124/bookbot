from stats import num_of_words



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    




def main():
    book_text = get_book_text("books/frankenstein.txt")
    print (f"{num_of_words(book_text)} words found in the document")



if __name__ == "__main__":
    main()