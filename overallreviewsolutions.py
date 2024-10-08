# Problem 1: Count Words in a Sentence
# -----------------------------------
# Directions:
# Write a function `count_words` that takes a string as input and returns
# the number of words in the string. Assume words are separated by spaces.
#
# Example Input:
# "The quick brown fox jumps over the lazy dog"
#
# Example Output:
# 9
def count_words(s: str) -> int:
    spaces = s.count(' ')
    spaces = spaces + 1
    return spaces
# Test Case
print(count_words("The quick brown fox jumps over the lazy dog"))

# Problem 2: Layered Triangle
# -----------------------------------
# Directions:
# Write a function `print_triangle` that takes an integer `n` as input
# and prints a right-aligned triangle with `n` layers.
#
# Example Input:
# n = 4
#
# Example Output:
#    *
#   **
#  ***
# ****
def print_triangle(n: int):
    for i in range(1, n+1):
        print(" "*(n-1)+"*"*i)

# Test Case
print_triangle(4)


# Problem 3: Palindrome Checker with Spaces Ignored
# -----------------------------------
# Directions:
# Write a function `is_palindrome` that takes a string and returns `True`
# if the string is a palindrome, ignoring spaces and capitalization.
# Return `False` otherwise.
#
# Example Input:
# "A man a plan a canal Panama"
#
# Example Output:
# True
def is_palindrome(s: str) -> bool:
    string = s.replace(" ", "").lower()
    return string == string[::-1]

# Test Case
print(is_palindrome("A man a plan a canal Panama"))

# Problem 4: Remove Duplicates from a List
# -----------------------------------
# Directions:
# Write a function `remove_duplicates` that takes a list of integers and
# returns a new list with all duplicates removed, keeping the original order.
#
# Example Input:
# [1, 2, 2, 3, 4, 4, 5]
#
# Example Output:
# [1, 2, 3, 4, 5]
def remove_duplicates(lst: list) -> list:
    seen= []
    unique_list = []
    for num in lst:
        if num not in seen:
            unique_list:append(num)
            seen.append(num)
        return unique_list
# Test Case
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# Problem 5: Find the Longest Word in a Sentence
# -----------------------------------
# Directions:
# Write a function `longest_word` that takes a string (sentence) as input
# and returns the longest word in the sentence. If two or more words have
# the same length, return the first one.
#
# Example Input:
# "The quick brown fox jumps over the lazy dog"
#
# Example Output:
# "jumps"
def longest_word(s: str) -> str:
    # Split the sentence into words
    words = s.split()

    # Initialize variables to keep track of the longest word
    longest = ""

    # Iterate through each word to find the longest one
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
# Test Case
print(longest_word("The quick brown fox jumps over the lazy dog"))


# Problem 6: Generate a List of Squares
# -----------------------------------
# Directions:
# Write a function `list_of_squares` that takes an integer `n` and returns
# a list of the squares of numbers from 1 to `n`.
#
# Example Input:
# n = 5
#
# Example Output:
# [1, 4, 9, 16, 25]
def list_of_squares(n: int) -> list:
    squares_list = []
    for i in range (1,n+1):
        squares_list.append(i**2)
    return squares_list

# Test Case
print(list_of_squares(5))