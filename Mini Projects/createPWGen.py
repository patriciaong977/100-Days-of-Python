# Day 5: Create a Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = "" # Empty string to hold the password.

#Easy Level - Order not randomized:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Letters
# for char in range(1, nr_letters + 1): # nr_letters + 1 because we want to include the last letter
#   password += random.choice(letters) # Randomly choose a letter from the list.

# # Symbols
# for char in range(1, nr_symbols + 1): # nr_symbols + 1 because we want to include the last symbol
#   password += random.choice(symbols) # Randomly choose a symbol from the list.

# # Numbers
# for char in range(1, nr_numbers + 1): # nr_numbers + 1 because we want to include the last number
#   password += random.choice(numbers) # Randomly choose a number from the list.

#Hard Level - Order of characters randomized:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Use a list to hold the characters.
pw_List = []

# Add the letters to the list.
for char in range (1, nr_letters + 1):
  pw_List.append(random.choice(letters)) # Randomly choose a letter from the list, and add it to the pw_List.
                                              # append() adds an item to the end of a list.
# Add the symbols to the list.
for char in range (1, nr_symbols + 1):
  pw_List.append(random.choice(symbols)) # Randomly choose a symbol from the list, and add it to the pw_List.

# Add the numbers to the list.
for char in range (1, nr_numbers + 1):
  pw_List.append(random.choice(numbers)) # Randomly choose a number from the list, and add it to the pw_List.


# print(pw_List) - To see the list of characters randomly chosen.
# Use another random module to randomize the order of the characters.
random.shuffle(pw_List) # Shuffles the list.

# Put the characters in the password.
for char in pw_List:
  password += char # Add each char on the list to the password string.

# Print the password.
print(f"Your password is: {password}")


# Documentation used to check shuffle:
# https://docs.python.org/3/library/random.html
