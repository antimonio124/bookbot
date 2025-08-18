from stats import num_of_words
from stats import times_each_character_appears
from stats import sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    




def main():
    book_text = get_book_text("books/frankenstein.txt")
    dic = times_each_character_appears(book_text)
    sorted_dic = sorted_dictionary(dic)
    # Displaying the results
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"Found {num_of_words(book_text)} total words")
    print("--------- Character Count -------")
    print(sorted_dic)


if __name__ == "__main__":
    main()