# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (year % 4) == 0:  # Is the year evenly divisible by 4?
    if (year % 100) == 0:  # Is it evenly divisible by 100?
        if (year % 400) == 0:  # Is the year evenly divisible by 400?
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
