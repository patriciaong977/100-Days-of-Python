import random

#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []  # Create an empty List called display.
length_Of_Word = len(chosen_word) # Need the length of word chosen to make the range.

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for eachLetter in range(length_Of_Word): # for each letter in the range of the length of the word.
  display += "_"

print(display)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for pos in range(length_Of_Word): # for each position in the length of the word
  letter = chosen_word[pos] # Save the value/letter to the var.
  if letter == guess: # if letter == guess
    display[pos] = letter # Replace the "_" with the actual letter



# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# Using for loops for the chosen_word.
# Reference: https://developers.google.com/edu/python/lists#for-and-in
# for inputLetter in chosen_word: # for each letter in the chosen word
#     if inputLetter == guess:  # if the letter in the chosen word is the same as the user's guess
#         print("Correct!")
#     else:
#         print("Incorrect!")

#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
