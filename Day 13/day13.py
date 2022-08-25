#### Debugging ####

# 1. Describe the problem.
  # Untangle the problem and find the root cause.
"""
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
"""

# What's the problem?
  # The problem is that "You got it" is not printed in the console.
# What is the for-loop doing?
  # The for-loop is going through a range from 1 to 20.
# When is the function meant to print "You got it"?
  # The function is meant to print at 20.
  # But the 20 is not included in the range because its an upper bound.
  # Technically the range is from 1-19.
# What are your assumptions about i?
  # The assumption is that i will reach 20.
  # But the range is 1-20, meaning 0-19. The upper bound is not included in the range.

# Fixing the code.
# def my_function():
#   for i in range(1, 20):
#     if i == 19:
#       print("You got it")

# my_function()

# 2. Reproduce the Bug
"""
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
"""

# randint will return a random number between 1 and 6.
# Reproducing the bug, test dice_num = 1, dice_num = 2,..., dice_num = 6.
  # dice_num = 6 --- Produces an error called IndexError: list index out of range.
  # 6 cannot be used because lists

# # Fixing the code.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# # dice_num = 6  # Produces an error.
# print(dice_imgs[dice_num])


# 3. Play Computer
  # Pretending to computer read, imagining how the computer would read the code.
"""
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
"""

# What's the problem?
  # Inputting 1994 will not print anything.

# # Fixing the code.
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")


# 4. Fix the Errors
  # Fix the errors first before you continue.
"""
age = input("How old are you? ")
if age > 18:
print("You can drive at age {age}.")
"""

# What's the problem?
  # There is an IndentationError: unexpected indent.
    # print statement is in the same line as if statement.
  # TypeError: '>' not supported between instances of 'str' and 'int'.
    # String Input (age) is being compared to an integer (18).
  # Print statement is not printing the value of age.
    # Print statement is not an f-string.

# # Fixing the code
# age = int(input("How old are you? "))  # Remember that input returns a string, convert string to integer.
# if age > 18:
#   print(f"You can drive at age {age}.")  # Indent this line.


# 5. Print is Your Friend
"""
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
"""

# What's the problem?
  # The problem is that the total_words is not printed in the console.
  # word_per_page variable is not updating.

# # Fixing the code
# pages = 0
# word_per_page = 0

# pages = int(input("Number of pages: "))
# # print(pages)
# word_per_page = int(input("Number of words per page: "))
# # print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)


# 6. Use a Debugger
  # PythonTutor, Thony, VSCode Debugging Tools.
  # Python Preview Extension on vscode.
  # Breakpoints, Debugger, and Debugging Tools.
"""
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
"""

# What's the problem?
  # The new item in the for loop is not being appended to the b_list.

# Fixing the code.
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # Append new_item to b_list.
  print(b_list)

mutate([1,2,3,5,8,13])


# Final Tips
# 7. Take a Break
# 8. Ask a Friend who's are developers.
  # They won't make the same assumptions as you do.
# 9. Run Often
  # Run the code often.
  # Run after every little execution.
# 10. Ask StackOverflow.
