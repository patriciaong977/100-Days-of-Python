# CalculatorApp
from calcArt import logo  # Import logo.
print(logo) # Show logo in the console.

# Adding
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

# Ask user for the first number.
num1 = int(input("Enter the first number: "))

# Print the different operations.
for symbol in operations:
  print(symbol)

# Ask user for an operation input.
operations_Input = input("Pick an operation from the list above: ")

# Ask user for the second number.
num2 = int(input("Enter the second number: "))

# Call the function using operations_Input in the operations dictionary.
calculation_result = operations[operations_Input]

answer = calculation_result(num1, num2) # Call the calculation_result function call.

# Print the result of the operation.
print(f"{num1} {operations_Input} {num2} = {answer}")
