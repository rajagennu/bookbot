#!/bin/env python3

import sys
from stats import get_num_words

# book_path = "./books/frankenstein.txt"

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

# reading the file
with open(book_path) as file:
    file_contents = file.read()

words = file_contents.split()

# print(len(words))

letter_count = get_num_words(words)

print("--- Begin report of " + book_path + " ---")
print(f"{len(words)} words found in the document")



for key, value in dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True)).items():
    if key.isalpha():
        print(f"'{key}: {value}'")

print("--- End report ---")
