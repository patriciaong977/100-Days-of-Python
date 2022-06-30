# Control flow and Logical Operators

# Control Flow with if/else and conditional operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

'''
# Comparison Operators are: >, <, >=, <=, ==, !=
# Remember indentation and blocks of code.

# If / else statement
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride. ")

# Modulo Operation - %
modulo = 7 % 2 # Divides 7 by 2, and give you the remainder.
# 2 + 2 + 2 + 1
# The result of the modulo will give you 1.
print(f"The result of the modulo is: {modulo}")

# Nested if / else
# Outside condition first, then inside condition.
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age <= 18:
      print("Please pay $7.")
    else:
      print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride. ")

# if /elif/ else
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
      print("Please pay $5.")
    elif age <= 18: # Catches between 12 and 18.
      print("Please pay $7.")
    elif age < 22:
      print("Please pay $10.")
    else:
      print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride. ")


# Multiple if
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
      bill = 5
      print("Child tickets are $5.")
    elif age <= 18:  # Catches between 12 and 18.
      bill = 7
      print("Youth tickets are $7.")
    else:
      bill = 12
      print("Adult tickets are $12.")

    # This applies to everyone's age.
    wants_photo = input("Do you want a photo taken? Y or N?")
    if wants_photo == "Y":
      bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride. ")


# Logical Operators - and, or, not
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
      bill = 5
      print("Child tickets are $5.")
    elif age <= 18:  # Catches between 12 and 18.
      bill = 7
      print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
      bill = 0
      print("Everything is going to be okay. Have a free ride on us!")
    else:
      bill = 12
      print("Adult tickets are $12.")

    # This applies to everyone's age.
    wants_photo = input("Do you want a photo taken? Y or N? ")
    if wants_photo == "Y":
      bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride. ")

'''

# lower() - converts to lowercase.
# count() - counts the number of times a character appears in a string.
