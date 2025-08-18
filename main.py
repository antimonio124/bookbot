from stats import num_of_words
from stats import times_each_character_appears


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    




def main():
    book_text = get_book_text("books/frankenstein.txt")
    dic = times_each_character_appears(book_text)
    print (f"{num_of_words(book_text)} words found in the document")
    print(dic)


if __name__ == "__main__":
    main()