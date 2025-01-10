#!/usr/bin/python3
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document \n")
    prt_report(char_count)

def prt_report(char_count):
    sort_char_dict = sorted(char_count, reverse=True, key=char_count.__getitem__)
    for char in sort_char_dict:
        print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report---")

def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()