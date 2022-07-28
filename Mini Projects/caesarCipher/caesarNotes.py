# Open caesarCipher.py while studying these code.
########## Separate Encrypt and Decrypt functions ##############

# # Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_Text, shift_amt):
#     # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     encrypt_Text = ""  # Placeholder for encrypted text.

# # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# # The index is out of range because of z.
#     for letter in plain_Text:
#         index_Alphabet = alphabet.index(letter)  # If letter = a, index = 0.
#         # Using modulus 26 to wrap around the alphabet.
#         index_New = (index_Alphabet + shift_amt) % 26
#         encrypt_Text += alphabet[index_New]
#     print(f"The encoded text is {encrypt_Text}.")

# #  Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(encrypt_Text, shift_amt):
#     # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#     plain_Text = ""  # Placeholder for plain text.

#     for letter in encrypt_Text:
#         index_Alphabet = alphabet.index(letter)
#         index_New = (index_Alphabet - shift_amt) % 26 # Subtract the shift_amt from the index_Alphabet.
#         # Add the letter_New to the plain text.
#         plain_Text += alphabet[index_New]
#     print(f"The decoded text is {plain_Text}.")


# # Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#     encrypt(plain_Text=text, shift_amt=shift)
# elif direction == "decode":
#     decrypt(encrypt_Text=text, shift_amt=shift)

################################################################################################
# Notes:
# Doesn't work with the word "civilization"
# For each letter in the plain text,
# for letter in plain_text:
#   # Shift it forward in the alphabet by the shift amount.
#   index_Alphabet = alphabet.index(letter) # Get the index of the letter in the alphabet.
#   index_New = index_Alphabet + shift_amt # Add the shift_amt to the index_Alphabet.
#   letter_New = alphabet[index_New] # Get the letter at the index_New. If index_New = 3, letter_New = d.
#   encrypt_Text += letter_New # Add the letter_New to the encrypted text.
# print(f"The encoded text is {encrypt_Text}")

# How modulus works:
# Ex: If shift_amt < 26: 24 % 26 = 24.
# 24/26 = 0.923077
# 0 x 26 = 0,
# 24 - 0 = 24
# Ex: If shift_amt = 26: 26 % 26 = 0.
# 26/26 = 1.
# 1 x 26 = 26,
# 26 - 26 = 0
# Ex: If shift_amt > 26: 34 % 26 = 8.
# 34/26 = 1.176471 = 1
# 1 x 26 = 26
# 34 - 26 = 8
# Ex: If shift_amt = high number: 9999 % 26 = 15.
# 9999/26 = 384.576923 = 384
# 384 x 26 = 9984
# 9999 - 9984 = 15
# Add the letter_New to the encrypted text.
