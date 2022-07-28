import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []  # Create an empty List called display.
# Need the length of word chosen to make the range.
length_Of_Word = len(chosen_word)

# For each letter in the chosen_word, add a "_" to 'display'.
# for each letter in the range of the length of the word.
for eachLetter in range(length_Of_Word):
    display += "_"
print(display)

# Use a while loop to keep asking the user for a guess until they guess the correct word.
game_over = False  # Use a variable to keep track if the game is over or not.

while not game_over:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # Check if the guess is in the chosen_word.
    # for each position in the length of the word.
    for pos in range(length_Of_Word):
        letter = chosen_word[pos]  # Save the value/letter to the var.
        if letter == guess:  # if letter == guess
            display[pos] = letter  # Replace the "_" with the actual letter.
        # Print 'display'. Show correctly guessed letters and the remaining "_"
    print(display)

    # Check if there are no more "_" in the display.
    if "_" not in display:
        game_over = True
        print("You win!")

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# Using for loops for the chosen_word.
# Reference: https://developers.google.com/edu/python/lists#for-and-in
# for inputLetter in chosen_word: # for each letter in the chosen word
#     if inputLetter == guess:  # if the letter in the chosen word is the same as the user's guess
#         print("Correct!")
#     else:
#         print("Incorrect!")
