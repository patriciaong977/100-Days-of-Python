# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# Can't use both of these.
# len() - gets the size of a particular list.
# sum() - returns a numbered sum of iterable items.

# Use for loop to calculate the average height.
# Round to the nearest whole number.

sum_height = 0  # Store total height.
sum_list = 0 # Number of items in the list.
total_Avg = 0 # Store the average height.

# For each item in student_heights:
for h in student_heights:
    sum_height += h  # Sum of items in the list.
    sum_list += 1  # Add +1 to indicates the num of items on the list.

# Calculate the average height.
total_Avg = round(sum_height/sum_list)

print(total_Avg) # Print the average height.

# For debugging:
# print(type(sum_height))
# print(type(sum_list))


# Shorcut: Using different functions.
# sum_height = sum(student_heights) # Sum of items in the list.
# sum_list = len(student_heights) # Num of students in the list.
# total_Avg = round(sum_height/sum_list) # Calculate the average height.
# print(total_Avg)
