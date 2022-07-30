#from replit import clear
#HINT: You can call clear() to clear the output in the console.

#################################################
from os import system, name # Using vs code, had to create own clear function.

# Clear Function
def clear():
  # For windows.
  if name == 'nt':
    _ = system('cls') # For some reason, had to switch clear and cls.
  # For Unix and Linux
  else:
    _ = system('clear')

#################################################

from bArt import logo # Import the logo from bArt.py

# Show logo in the console.
print(logo)

# Loop to find the highest bid.
def highest_bidder(bidding_Dict):
  highest_Bid = 0  # Create a variable to store the highest bid.
  winning_Bidder = ""  # Create a variable to store the winning_Bidder.

  # bidding_Dict = {"Isha": 100, "Andrew":200}
  for bidName in bidding_Dict:  # For each bidName in the bidding_Dict.
    bidAmt = bidding_Dict[bidName]  # The bidAmt is the value of the bidName.
    if bidAmt > highest_Bid: # If the bidAmt is greater than the highest_Bid.
      highest_Bid = bidAmt # The highest_Bid is the bidAmt.
      winning_Bidder = bidName # The winning_Bidder is the bidName.

  # Print the winning_Bidder and highest_Bid.
  print(f"The winner is {winning_Bidder} with a bid of ${highest_Bid}.")


# Loop to continue asking for more bids and bidders.
total_Bids = {}  # Create an empty dictionary to store name and bid_price.
continue_loop = True

while continue_loop:
  bidderName = input("What is your name? ")
  # Make sure price input is integer.
  bidderPrice = int(input("How much would you like to bid? $"))

  # Add the bidderName and bidderPrice to the empty dictionary total_Bids.
  total_Bids[bidderName] = bidderPrice

  # Ask user if there are any more bidders.
  more_Bidders = input("Are there any more bidders? Type 'yes' or 'no'. \n ")

  # If there are more bidders, continue the loop,
  if more_Bidders == "yes":
    clear() # Clear the console for the next bidder.
  else: # If there are no more bidders, break the loop.
    continue_loop = False
    # Call the highest_bidder function to find the highest bid.
    highest_bidder(total_Bids) # Pass the dictionary.
