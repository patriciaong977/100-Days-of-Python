# Primitive Data Types

# String

print("Hello"[4])  # H

# Subscript - pulling an element out of a string.
# Subscripting starts at 0.

# Integers
# 123_456_789 = 123456789

# Floating Point Number - decimal numbers
# 3.14159

# Boolean - True or False, need to be capitalized.

street_name = "Abbey Road"  # The space is counted as a character, index[5].
print(street_name[4] + street_name[7])  # "y" + "o"

# Type Error, Type checking
num_char = len(input("What is your name? "))
# print ("Your name is " + num_char + " characters long.") # Type Error

# Use type() to check the type of a variable.
print(type(num_char))  # <class 'int'>

# Type Conversion
num_char = len(input("What is your name? "))
new_num_char = str(num_char)  # "123"
print("Your name is " + new_num_char + " characters long.")

# Can also convert other data types.
a = str(123)  # "123", converts integer to string.
print(type(a))  # <class 'str'>

print(70 + float("100.5"))  # Converting 100.5 to a float, then adding 70.
print(str(70) + str(100))  # "70100" that's a string, concatenating strings.


# Mathematical Operations in Python
# +, - , * , /
print(type(6 * 5))  # Results in an int.
print(type(6 / 3))  # Results in a float.

# ** - Exponents
print(2 ** 3)  # Means 2^3 = 8
print(3 ** 2)  # Means 3^2 = 9

# Remember PEMDASLR! (), **, * /, + - [Remember most leftest first.]
print(3 * 3 + 3 / 3 - 3)  # Multiply, Divide, Add, Subtract. = 7.0
print(3 * (3 + 3) / 3 - 3)  # Add, Multiply, Divide, Subtract = 3.0

a = int("5") / int(2.7)
print(type(a))  # It becomes a float. Because of division.
print(a)

# Number Manipulation and FStrings
print(8/3)  # 2.6666666666666665

# Round() - Rounds to the nearest integer or specified number of decimal places.
print(round(8 / 3))  # 3
print(round(8 / 3, 2))  # Round to a given number of decimal places.

# Trunc() - Truncates the decimal, drop the fractional part.
# Rounds up or down towards zero.

# Floor division - //
print(8 // 3)  # Will give you a whole number (int).

# Shorthand Operators
result = 4 / 2
result /= 2  # Same as result = result / 2
print(result)


# F-Strings
score = 0        # int
height = 1.8     # float
isWinning = True  # bool

print(
    f"Your score is {score}, your height is {height}, you are winning is {isWinning}.")
