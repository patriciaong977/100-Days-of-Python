#from replit import clear
#HINT: You can call clear() to clear the output in the console.

#################################################
import os # For clear function

os.system('clear')

# to make it in a function
def clear():
  os.system('clear')

# Call the clear function.
# clear()
#################################################

from bArt import logo # Import the logo from bArt.py

# Show logo in the console.
print(logo)

total_Bids = {}  # Create an empty dictionary to store name and bid_price.


# Loop to find the highest bid.
def highest_bid(total_Bids):
  highest_Bidder = 0  # Create a variable to store the highest bidder.
  wining_Bidder = ""  # Create a variable to store the wining bidder.

  for bid_name in total_Bids: # If the bid_name is in the dictionary,
    bid_price = total_Bids[bid_name]  # Get the bid_price.

    if bid_price > highest_bidder:  # If the bid_price is greater than the highest_bidder,
      highest_bidder = bid_price  # Set the highest_bidder to the bid_price.
      wining_Bidder = bid_name
    print(f"The winner is {wining_Bidder} with a bid of ${highest_bidder}.")


# While loop to ask for more bids.
more_Bids = True

while more_Bids:
  name = input("What is your name?")
  bid_price = int(input("What is your bid price? $"))

  # Add key and value to the dictionary. Key = name, value = bid_price.
  total_Bids[name] = bid_price

  # Ask if there are more bidders.
  continue_loop = input("Are there any other bidders? Type 'y' or 'n'.")

  # If there are more bidders, clear()
  if continue_loop == "y":
    clear()
  else: # If there are no more bidders, more_Bids = False and call highest_bid().
    more_Bids = False
    # Call highest_bid function.
    highest_bid(total_Bids)
