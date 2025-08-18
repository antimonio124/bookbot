def num_of_words(book_text):
    return len(book_text.split())

def times_each_character_appears(book_text):
    dictionary = {}
    for char in book_text:
        book_text = book_text.lower()
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary