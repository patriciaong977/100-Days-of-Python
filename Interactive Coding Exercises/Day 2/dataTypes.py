# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
firstDigit = int(two_digit_number[0])  # Get the first digit.
secondDigit = int(two_digit_number[1])  # Get the second digit.

# print(type(two_digit_number[0])) # Checking the type of two_digit_number.
# print(type(firstDigit)) # Checking if type conversion works.

sum = firstDigit + secondDigit
print(sum)
