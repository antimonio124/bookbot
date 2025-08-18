import sys
from stats import num_of_words
from stats import times_each_character_appears
from stats import sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    




def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <book_file>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    dic = times_each_character_appears(book_text)
    sorted_dic = sorted_dictionary(dic)
    # Displaying the results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print (f"Found {num_of_words(book_text)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_dic:
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            None
            


if __name__ == "__main__":
    main()