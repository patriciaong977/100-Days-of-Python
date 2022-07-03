#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

#Write the rest of your code below this line 👇

# Generate a random integer between 0 to 1.
random_HT = random.randint(0, 1)

if random_HT == 1:  # If 1, Heads.
    print("Heads")
else:  # Else, Tails.
    print("Tails")
