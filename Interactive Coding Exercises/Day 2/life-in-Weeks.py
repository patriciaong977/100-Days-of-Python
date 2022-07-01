# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Input is always a string val, unless specified.
# Convert age into an int.
age = int(age)
new_age = 90 - age  # Only live until 90 years old.

# Convert age into days. 1 year = 365 days
age_in_Days = new_age * 365

# Convert age into weeks. 1 year = 52 weeks.
age_in_Weeks = new_age * 52

# Convert age into months. 1 year = 12 months.
age_in_Months = new_age * 12

# Print results
print(
    f"You have {age_in_Days} days, {age_in_Weeks} weeks, and {age_in_Months} months left.")
