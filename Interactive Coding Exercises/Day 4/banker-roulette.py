import random
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Need to know the length of the list
list_length = len(names)

# Randomize. Index starts at 0, so subtract 1 from the length.
rand_choice = random.randint(0, list_length - 1)

# Choose who will pay
person_pay = names[rand_choice]

# Print
print(f"{person_pay} is going to buy the meal today!")


'''
 Second Solution:
 person_pay = random.choice(names)
 print(person_pay + " is going to buy the meal today!")
'''
