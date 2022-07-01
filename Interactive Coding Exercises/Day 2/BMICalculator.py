# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Check input type
# print(type(height))
# print(type(weight))

# Convert height and weight to float
height = float(height)
weight = float(weight)

# # Check if conversion happened.
# print(type(height))
# print(type(weight))

# Calculate for BMI and Convert to Int.
BMI = int(weight / (height ** 2))
print(BMI)
