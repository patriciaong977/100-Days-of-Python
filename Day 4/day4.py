# Randomization and Python Lists
# Documentation on Random: https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# Deterministic - does actions in a predictable way.
# Pseudorandom number generator - generates random numbers (Python's random module)
# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

import random  # Import the random module.
# import my_module # Import the my_module module.

'''
# Calls random module.randomfunction(x,y)
random_int = random.randint(1, 10) # Generate a random integer between 1 and 10.
print(random_int)

# Module - a collection of functions.
# print(my_module.pi)


# Random.random() - returns the next random floating point number in the range [0.0, 1.0).
  # 0.000000 to 0.999999...
random_float = random.random()
print(random_float)

# What if you want a random floating number between a certain range? 0-5?
random_float * 5 # 0.000000 to 4.999999... This is how we expand the range.


# Looking at the love calculator:
love_score = random.randint(1, 100) # Generate a random integer between 1 and 100.
print(f"Your love score is: {love_score}")



# Python Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina",
                     "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
                     "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]
print(states_of_america) # Print the list.

# To specifically print out a certain item in the list, use the index.
print(states_of_america[39]) # Prints out the item at index 39.
print(states_of_america[-2]) # Prints out the item starting from the last item. "Alaska"
print(states_of_america[0:5]) # Prints out the first 5 items.

# Change the value of an item in the list.
states_of_america[01] = "Pencilvania"

# Append() - adds an item to the end of the list.
states_of_america.append("Angelaland")

# More about lists: https://docs.python.org/3/tutorial/datastructures.html


# Index out of range.
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#                "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery",
#                "Potatoes"]

# Nested list - A list within a list.
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # Two other lists inside a list.

print(dirty_dozen)


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes",
# "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# What does the above print?
# ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches",
# "Cherries", "Melons", "Lemons"]


# fruits = ["Strawberries", "Nectarines", "Apples",
#           "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])

# What does the above print?
# Kale

'''

