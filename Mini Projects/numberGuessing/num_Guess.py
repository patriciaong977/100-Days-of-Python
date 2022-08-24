#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


###### Import ######
from num_guess_Art import logo  # Import the logo num_guess_Art.
from random import randint  # Import the randint function from the random module.


###### Global Variables ######
EASY_MODE_GUESS = 10  # Num of guesses in easy mode.
HARD_MODE_GUESS = 5  # Num of guesses in hard mode.


###### Functions ######
def set_difficulty(): # Set the difficulty of the game.s
  level = input("Please select a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    print("You have 10 guesses.")
    return EASY_MODE_GUESS
  elif level == "hard":
    print("You have 5 guesses.")
    return HARD_MODE_GUESS
  else:
    print("Invalid input. Please try again.")
    set_difficulty()

def guess_Number(): # Guess the number.
  guess = int(input("\nPlease guess a number between 1 and 100: "))
  return guess

def check_Guess(amt_guess_left, answer, usr_guess): # Check the guess.
  if usr_guess > answer:
    amt_guess_left -= 1
    print(f"\nToo high. You have {amt_guess_left} guesses left.")
    return amt_guess_left
  elif usr_guess < answer:
    amt_guess_left -= 1
    print(f"\nToo low. You have {amt_guess_left} guesses left.")
    return amt_guess_left


def start_Game(): # Start the game.
  print(logo) # Print the logo
  print(f"\nWelcome to the Number Guessing Game!\n")  # Welcome Message

  amt_guess_left = set_difficulty()  # Set the difficulty (amt of guesses) in the game.

  print(f"\nComputer is now choosing a number between 1 and 100.\n")
  answer = randint(1, 100)  # Generate a random number between 1 and 100.
  print(f"This is the {answer}")  # Print the answer.

  usr_guess = guess_Number()  # Ask the player to guess the number. Holds the user's guess.

  # Loop through the game until the player guesses the number or runs out of guesses.
  while usr_guess != answer:
    # Check the guess.
    amt_guess_left = check_Guess(amt_guess_left, answer, usr_guess)
    if amt_guess_left == 0: # If the player runs out of guesses, break the loop.
      print(f"\nYou ran out of guesses. The answer was {answer}.")
      return
    elif amt_guess_left > 0:  # If the player has guesses left, ask them to guess again.
      usr_guess = guess_Number()  # Ask the player to guess the number again.

  print(f"\nYou got it! The answer is {answer}.") # If usr_guess == answer, print the answer.

start_Game() # Call the start_Game function.
