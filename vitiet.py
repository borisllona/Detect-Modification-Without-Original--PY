#!/usr/bin/env python3
"""
   Lead table modifier
"""

import sys
import random
import string

def create_character():
    """Function to create a character in Lead table domain"""
    domain = string.ascii_uppercase + string.digits
    return random.choice(domain)

def noise(text, prob_soroll=0.1):
    """Adds noise to the text"""
    text_list = list(text)
    if random.random() < prob_soroll:
        character = create_character()
        position = random.randint(0, len(text_list)-1)
        text_list[position] = character
    return ''.join(text_list)

def main():
    """Reads a file from stdin and writes the same file to stdoud with noise addition"""
    original_file = sys.stdin
    modified_file = sys.stdout
    noise_prob = float(sys.argv[1])

    original_text = original_file.read()
    sent_text = noise(original_text, noise_prob)
    print(sent_text, file=modified_file, end='')

if __name__ == "__main__":
    main()
