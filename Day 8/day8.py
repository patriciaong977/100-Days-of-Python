# Functions with Inputs
# Arguments with Parameters

# Review:
# def greet():  # Create a function called greet()
#   # Write 3 print statements inside the function.
#   print("Hello")
#   print("Have a nice day!")
#   print("Goodbye!")

# greet()  # Call the greet() function and run your code.

# Function with Inputs
# Can create Function that allows for input. This is called a "parameter".
# def greet_with_name(name):  # name = parameter
#   print("Hello " + name)
#   print(f"Have a nice day {name}!")

# greet_with_name("John") # "John" = argument


# Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name} from {location}!")

greet_with("John", "New York")  # Positional Arguments - position matters.
greet_with(name="John", location="California")  # Keyword arguments - doesn't matter if order is wrong.
