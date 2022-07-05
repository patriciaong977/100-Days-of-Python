# Day 4 Project: Rock Paper Scissors

# Import the random module for computer choices.
import random

# ASCII Art for Rock Paper Scissors:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line

rps_ASCII = [rock, paper, scissors] # Create a list of the ASCII art for each of the three choices.

# Print user choice, if invalid, print error message.
while True:
  try:
    # Has the user input their choice, convert to int.
    p_choice = int(input(
        "Please choose 0 for Rock, 1 for Paper, or 2 for scissors: \n"))

    # If statement to check. If valid, print the user choice and break out of the loop.
    if p_choice == 0 or p_choice == 1 or p_choice == 2:
        print(rps_ASCII[p_choice]) # Print the ASCII art for the user choice.
        break
    else:
        print("Invalid input.")  # If invalid, print error message.
  except:  # If invalid, print error message.
    print("Provide a valid integer input.")
    continue  # Loop back to the beginning, and ask for input again.

# Generate the computer's choice by using random.
c_choice = random.randint(0, 2) # Generate a random integer between 0 and 2.
print("Computer chooses: \n")
print(rps_ASCII[c_choice]) # Print the computer's choice.

# If statement to determine the winner.
# If p == c its a tie, 0 beats 2, 2 beats 1, 1 beats 0. Else, you lose.
if p_choice == c_choice:
  print("It's a tie!")
elif p_choice == 0 and c_choice == 2:
  print("You win!")
elif p_choice == 2 and c_choice == 1:
  print("You win!")
elif p_choice == 1 and c_choice == 0:
  print("You win!")
else:
  print("You lose!")
