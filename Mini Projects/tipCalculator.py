# Day 2 Project: Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number.
# You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Welcome Message
print("Welcome to the tip calculator! ")

# Ask how much the total bill is.
bill_Total = float(input("What was the total bill? $"))

# Ask how much tip in percent would they like to give?
tip_Int = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Ask how many people are splitting the bill.
people_split_bill = int(input("How many people to split the bill? "))

# Convert tip_Int to tip_Decimal
tip_Decimal = tip_Int / 100

# Calculate the tip.
tip_Total = bill_Total * tip_Decimal

# Calculate the bill_Total + tip_Total.
bill_Total += tip_Total

# Calculate the split of the bill.
split_Total = bill_Total / people_split_bill

# Round the bill to two decimal places.
rounded_Total = round(split_Total, 2)

# Print the result
# print(f"Each person should pay: ${rounded_Total}")
  # This results to a formatting problem when you input the following:
    # 100, 10, 4 = $27.5, so use str_format instead.

# Using str format to round the decimal places. To display if $27.50
str_format_Total = "{:.2f}".format(split_Total) # 2 decimal places.
print(f"Each person should pay: ${str_format_Total}")
