def print_upper_words(words, first_letters):
    """Prints each word in list capitalized if it starts with a declared letter"""

    for word in words:
        for letter in first_letters:
            if word[0] == letter:
                print(word.capitalize())


print_upper_words(['peter', 'aurora', 'perry', 'alex', 'jon'],{'a','p'})