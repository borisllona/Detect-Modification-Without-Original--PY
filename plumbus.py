#!/usr/bin/env python3
"""
   Lead table generator
"""

import random
import sys
import string

outputfile = open("original.txt","w")#sys.stdout

# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def create_word(word_length):
    """Function to create a word in Lead table domain"""
    domain = string.ascii_uppercase + string.digits
    return ''.join(random.choice(domain) for _ in range(word_length))

#''.join(random.choices(string.ascii_uppercase + string.digits, k=word_length))

def emisor():
    """Generator for several words"""
    while True:
        yield create_word(random.randint(1, 12))

def main():
    """Main function"""
    if len(sys.argv) > 1:
        total_words = int(sys.argv[1])
    else:
        total_words = 25

    emisor_generator = emisor()
    original_text = ' '.join([next(emisor_generator) for x in range(total_words)])
    print(original_text)
    outputfile.write(original_text)

if __name__ == "__main__":
    main()
