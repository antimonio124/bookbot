def num_of_words(book_text):
    return len(book_text.split())

def times_each_character_appears(book_text):
    dictionary = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary