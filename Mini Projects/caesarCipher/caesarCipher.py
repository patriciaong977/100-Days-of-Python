# Day 8 Project: Caesar Cipher
# Check caesarNotes.py for more information.

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# Import art from caesarArt.py.
from caesarArt import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Combine encrypt and decrypt functions into one function called 'caesar()'.
def caesar(input_Text, input_Shift, input_Direction):
  result_Text = ""  # Result text when encoded or decoded.

  # Loop through each character in the input text.
  for letter in input_Text: # For each letter in the input text.
    # Check if letter is in the alphabet. If letter is in alphabet.
    if letter in alphabet:
      index_Alphabet = alphabet.index(letter) # Take the index of the letter in the alphabet.
      # Encode or decode the letter.
      if input_Direction == "encode":
        index_New = (index_Alphabet + input_Shift) % 26 # Calculate the new index of the letter.
        result_Text += alphabet[index_New]  # Add the new letter to the result text.
      elif input_Direction == "decode":
        index_New = (index_Alphabet - input_Shift) % 26 # Calculate the new index of the letter.
        result_Text += alphabet[index_New]  # Add the new letter to the result text.
    else: # If the letter is not in the alphabet.
      result_Text += letter # Add the letter to the result text.

  print(f"Here's the {input_Direction}d result: {result_Text}.")


#  Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
loop_Cipher = True

while loop_Cipher: # While the loop_Cipher is true, keep looping.
  # Ask for the Inputs again.
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  # Check if the direction is valid.
  while direction != "encode" and direction != "decode" :
    print("Invalid input. Please try again.")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Call the caesar() function.
  caesar(input_Text = text, input_Shift = shift, input_Direction = direction)

  # Ask the user if they want to continue.
  continue_Cipher = input(
      "Do you want to do another cipher? Type 'yes' if you do. Otherwise type 'no':\n")
  if continue_Cipher == "no": # if continue_Cipher is 'no', break the loop.
      loop_Cipher = False
      print("Goodbye! Thanks for using the Caesar Cipher!")
