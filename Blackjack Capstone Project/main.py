############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############# Blackjack Project #############

### Imported Libraries ###
from art import logo  # Import logo from art.py
import random # Import random library. (To choose randomly from deck of cards)


### Variables ###
player_cards = []  # Create a list to hold the player's cards.
dealer_cards = []  # Create a list to hold the dealer's cards.


### Functions ###
def deal_card():
  """ Deals a random card from the list of cards in the deck.

  Returns:
      random_Card (int): Returns a random integer from the deck of cards.
  """
  deck_of_Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Create the deck of cards. Represent Ace with 11, 10/Jack/Queen/King with 10.
  random_Card = random.choice(deck_of_Cards)  # Choose a random card from the deck of cards.
  return random_Card

def calculate_Hand(list_of_Cards):
  """ Takes a list of cards as the input and returns the sum of the Hand.

      Checks for a blackjack (a hand with only 2 cards: ace + 10) and returns 0 instead of the actual score.
      0 will represent a blackjack in the game.

      Checks for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.

  Returns:
    hand_Sum (int) : Returns the sum of the list of cards.
  """
  hand_Sum = 0 # Create a variable to hold the sum of the Hand.

  # Sum the list of cards.
  for card in list_of_Cards: # For each card in the list of cards...
    hand_Sum += card # Add the card to the sum of the Hand.

  # Check the hand_Sum for a blackjack.
  if hand_Sum == 21 and len(list_of_Cards) == 2:
    return 0

  # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if 11 in list_of_Cards and hand_Sum > 21:
    list_of_Cards.remove(11)
    list_of_Cards.append(1)

  return hand_Sum


# For loop to deal the player and dealer 2 cards each.
for i in range(2):
  player_cards.append(deal_card()) # Add the random card to the player's cards list.
  dealer_cards.append(deal_card()) # Add the random card to the dealer's cards list.

# Checking
print(player_cards)
print(dealer_cards)

calculate_Hand(player_cards) # Call the function to calculate the score of the player and dealer.

if calculate_Hand() == 0: # If the player has a blackjack...
  print("Blackjack! You win!") # Print "Blackjack! You win!"
else:
  print("You lose!") # Else, print "You lose!"
