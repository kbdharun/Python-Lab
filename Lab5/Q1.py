# Q1. 

'''
Create list of list to store set of words. Write a recursive function to check every word is palindrome
or not. Include a recursive function in another separate module by receiving list item as an argument.
'''

from palindrome import is_palindrome

# Get user input to get list of words
num_lists = int(input("How many lists of words do you want to check? "))
words = []
for i in range(num_lists):
    word_list = input(f"Enter space-separated words for list {i+1}: ").split()
    words.append(word_list)

# Recursive function to check palindromes
def check_palindrome(lst):
    for item in lst:
        if isinstance(item, list):
            check_palindrome(item)
        else:
            if is_palindrome(item):
                print(f"{item} is a palindrome")
            else:
                print(f"{item} is not a palindrome")

# Call function to check palindromes in list of words
check_palindrome(words)
