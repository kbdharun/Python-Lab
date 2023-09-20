# Q3.

'''
Create a List with N number of numerical values. Sort the list elements in ascending order using merge
sort. (don’t use built in function). Include a recursive function for merge sort in process module. Print
the sorted list normal module.
'''

# We import the module process.py to perform merge sort
import process

# User input for numbers
values_str = input("Enter a list of numerical values, separated by spaces: ")
values = [int(value) for value in values_str.split()]

# Sort the list using merge sort from process.py module
sorted_values = process.merge_sort(values)

# Printing the sorted list from process.py
print("Sorted values:", sorted_values)
