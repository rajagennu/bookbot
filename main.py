#!/bin/env python3

book_path = "./books/frankenstein.txt"

# reading the file
with open(book_path) as file:
    file_contents = file.read()

words = file_contents.split()

# print(len(words))

# empty dict

letter_count = {}

# count words 
for word in words:
    for char in word.lower():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

# print(letter_count)

print("--- Begin report of " + book_path + " ---")
print(f"{len(words)} words found in the document")



for key, value in dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True)).items():
    if key.isalpha():
        print(f"the '{key}' character was found {value} times")

print("--- End report ---")
