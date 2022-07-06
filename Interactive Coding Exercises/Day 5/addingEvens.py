# Write your code below this row 👇

even_Sum = 0  # Store the sum of the even numbers.

# Use range for a list of 1 - 100
for num in range(2, 101, 2):  # Start from 2 and skip by 2's.
    even_Sum += num  # Add the number to the sum.

print(even_Sum)  # Should print 2550.


# Another solution: Using modulo (%).
# total = 0
# for num in range(1, 101):
#   if num % 2 == 0: # If the remainder of num / 2 is 0,
#     total += num
# print(total)
