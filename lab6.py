import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex

# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1
class Book:
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title
def index_smallest_from(books:list[Book], start:int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None
    mindex = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx
    return mindex
def selection_sort_books(books:list[Book])->None:
    for idx in range(len(books) - 1):
        mindex = index_smallest_from(books, idx)
        tmp = books[mindex]
        books[mindex] = books[idx]
        books[idx] = tmp
#the function's purpose is to sort a list of books by title alphabetically
#the input is a list of books
#the output is a sorted list of books
#the parameter is type list[Book]
#None is returned since the list of books is sorted

# Part 2
def swap_case(letters:str)->str:
    result = []
    for character in letters:
        if character.islower():
            result.append(character.upper())
        elif character.isupper():
            result.append(character.lower())
        else:
            result.append(character)
    return ''.join(result)
#the function's purpose is to change lower letters to uppercase letters and vice versa
#the input is a string of characters
#the output is a string of characters
#the parameter is type string
#a string is returned

# Part 3
def str_translate(string:str, old:str, new:str)->str:
    result = []
    for char in string:
        if char==old:
            result.append(new)
        else:
            result.append(char)
    return ''.join(result)
#the function's purpose is to return a string where certain 'old' characters are replaced with'new'
#other characters remain the same
#the inputs are strings; old and new are single characters
#the output is a string
#the parameters are type string
#a string is returned

# Part 4
def histogram(string:str)->dict:
    word_count = {}
    words = string.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1 #increment
        else:
            word_count[word]=1
    return word_count

#the function's purpose is to take a string and return a dictionary that maps strings to integers
#the input is a string
#the output is a dictionary
#the parameter is type string
#a dictionary is returned