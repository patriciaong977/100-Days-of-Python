import random

# import hm_wordlist.py and hm_Art.py
from hm_wordList import word_list
from hm_Art import logo, stages

# Print Welcome logo
print(logo)

amt_lives = 6  # Set amount of lives to 6.
word_list = ["aardvark", "baboon", "camel"]  # Set a specific list of words.
# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
display = []  # Create an empty List called display.
# Getting the length of the chosen_word to make the range.
length_Of_Word = len(chosen_word)


# For Testing code, prints the random word chosen.
# print(f'Pssst, the solution is {chosen_word}.')


# Display "_" for each letter in the chosen_word.
# For each letter in the range of the length of the word.
for eachLetter in range(length_Of_Word):
    display += "_"  # Add "_" to the display list.
# print(display)

# Use a while loop to keep asking the user for a guess until they guess the correct word.
game_over = False  # Use a variable to keep track if the game is over or not.

while not game_over:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # Check if the guess letter is already guessed.
    if guess in display:
        print(f"You already guessed {guess}.")

    # Check if the guess letter is in the chosen_word.
    # For each position in the length of the word.
    for pos in range(length_Of_Word):
        letter = chosen_word[pos]  # Save the value/letter to the var.
        if letter == guess:  # if letter == guess
            display[pos] = letter  # Replace the "_" with the actual letter.
        # Print 'display'. Show correctly guessed letters and the remaining "_"
    # print(display)

    # Check if guess letter is not in the chosen_word, subtract 1 from amt_lives.
    if guess not in chosen_word:
        print(f"Sorry, {guess} is not in the word. You lose a life.")
        amt_lives -= 1  # Subtract 1 from amt_lives.
        # If lives == 0, print "Game Over" and break the loop.
        if amt_lives == 0:
            game_over = True  # Breaks the loop.
            print("You lose. Game Over.")

    # Join all the elements in display and turn it into a string.
    print(f"{' '.join(display)}")

    # Check if there are no more "_" in the display. Meaning the user has correctly guessed the word.
    if "_" not in display:
        game_over = True
        print("You win!")

    # Print the stage of the hangman according to the amt_lives left.
    print(stages[amt_lives])


# Using for and in.
# Reference: https://developers.google.com/edu/python/lists#for-and-in
