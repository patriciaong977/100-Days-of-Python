# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Calculate the BMI and round the result.
BMI = round(weight / (height ** 2))

# Print BMI Calculation
# print(f"{weight} / ({height} * {height} = {BMI})")

# Interpret BMI.
if BMI < 18.5:
    BMI_class = "are underweight."
elif BMI < 25:  # It already checks 18.5 and below above.
    BMI_class = "have a normal weight."
elif BMI < 30:
    BMI_class = "are slightly overweight."
elif BMI < 35:
    BMI_class = "are obese."
else:
    BMI_class = "are clinically obese."

# Print final line, round the bmi.
print(f"Your BMI is {BMI}, you {BMI_class}")
