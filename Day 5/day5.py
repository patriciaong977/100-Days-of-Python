# Python Loops
'''
# Using the For Loop with a List
# for item in list_of_items:
  # Do something to each item.


# Example
fruits = ["Apple", "Peach", "Pear"] # Create a list of fruits.
# For (name for a single item) in (name of list to go through):
for fruit in fruits: # Goes through each item in the list.
  print(fruit) # 0. Apple, 1. Peach, 2. Pear
  print(fruit + " Pie") # 0. Apple Pie, 1. Peach Pie, 2. Pear Pie
print(fruits) # ["Apple", "Peach", "Pear"]

# Remember Indentation is Important!
# Functions mentioned:
  # sum() - Returns the sum of a list of numbers.
  # len() - Returns the length of a list.
  # round() - Rounds a number to the nearest integer.
  # max() - Returns the largest number in a list.
  # min() - Returns the smallest number in a list.


# For loops and range() function
# range() - returns a sequence of numbers,
          # starting from 0 by default, and increments by 1 (by default),
          # and stops before a specified number.
# Range is helpful if you want a range of numbers to loop through.
# Syntax: range(start, stop, step)
  # for number in range (a, b):
    # print(number)

for number in range(1, 10): # Hold the numbers between 1 and 10.
  print(number) # Only prints: 1, 2, 3, 4, 5, 6, 7, 8, 9

for number in range(1, 10, 3):  # Hold the numbers between 1 and 10.
  print(number)  # Only prints: 1, 4, 7

# To print the sum of a list of numbers:
sum = 0 # Sum of the range between 1 - 100.
for number in range(1, 101):
  sum += number
print(sum)

'''

