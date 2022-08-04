# Imports
from os import system, name # For clear function.
from calcArt import logo  # Import logo.

######## Clear Function ########
def clear():
  # For windows.
  if name == 'nt':
    _ = system('cls')
  # For Unix and Linux
  else:
    _ = system('clear')


######## Operations Function ########
def add(n1, n2):
  """Add two numbers together."""
  return n1 + n2
# Subtracting
def subtract(n1, n2):
  """Subtract two numbers together."""
  return n1 - n2
# Multiplying
def multiply(n1, n2):
  """Multiply two numbers."""
  return n1 * n2
# Dividing
def divide(n1, n2):
  """Divide two numbers. """
  return n1 / n2

# Dictionary of operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
  }


######## Main Function ########
def calculator():
  print(logo)  # Show logo in the console.

  num1 = float(input("Enter the first number: ")) # Get the first number.
  # Print the operations from the dictionary to the console.
  for symbol in operations:
    print(symbol)
  should_continue = True # Create a variable to control the loop.

  # Loop to continue asking for more operations.
  while should_continue:
    operation_Input = input("Enter the operation: ") # Get the operation/key to access the dictionary.
    num2 = float(input("Enter the second number: ")) # Get the second number.

    # Perform the calculation.
    calculation_function = operations[operation_Input] # Using the operation_Input (Key), get the function.
    answer = calculation_function(num1, num2) # Perform the calculation.
    print(f"{num1} {operation_Input} {num2} = {answer}") # Print the answer.

    # Handle 'y' or 'n' input.
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
