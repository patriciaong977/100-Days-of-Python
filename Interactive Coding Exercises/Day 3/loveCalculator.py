# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Convert both names into lower-case and combine.
name1 = name1.lower()
name2 = name2.lower()
bothName = name1 + name2

# Count for TRUE, and add to the true_Sum
true_Sum = 0
true_Sum = bothName.count('t') + bothName.count('r') + \
    bothName.count('u') + true_Sum + bothName.count('e')

# Count for Love, and add to the love_Sum
love_Sum = 0
love_Sum = bothName.count('l') + bothName.count('o') + \
    bothName.count('v') + bothName.count('e')

# Combine true_Sum and love_Sum
love_Score = int(str(true_Sum) + str(love_Sum))

# Print messages
if (love_Score < 10) or (love_Score > 90):
    love_Msg = ", you go together like coke and mentos."
elif (love_Score >= 40) and (love_Score <= 50):
    love_Msg = ", you are alright together."
else:
    love_Msg = "."

print(f"Your score is {love_Score}{love_Msg}")
