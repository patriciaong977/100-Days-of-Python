# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]  # map [0]
row2 = ["⬜️", "⬜️", "⬜️"]  # map [1]
row3 = ["⬜️", "⬜️", "⬜️"]  # map [2]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# The input takes in a string. "21" is a string.

# Enter position you want the x to be at.
# Horizontal, position[0] is the first character of the string.
x = int(position[0])  # Convert the string to an int.
# Vertical, position[1] is the second character of the string.
y = int(position[1])  # Convert the string to an int.

# (Vertical, Horizontal)
# Row, Col
map[y-1][x-1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
