# Write your code below this line 👇

# To round up a number: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
import math  # For rounding

# Write a function that calculates the number of cans needed.
def paint_calc(height, width, cover):
    num_cans = math.ceil(((height * width) / cover)) # Rounding up - math.ceil()
    print(f"You'll need {num_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
