# Functions with Outputs
def my_function():
  result = 3 * 2
  return result # Output of the function.

# my_function() # Call the function.
  # The output of my_function is the result = 6.
  # You can also assign the output to a variable.
output_of_my_function = my_function()

# Function that takes an input and returns a string.
# def format_name(fName, lName):
# # Use title() - https://docs.python.org/3/library/stdtypes.html#str.title
#   format_fName = fName.title()
#   format_lName = lName.title()

#   return f"{format_fName} {format_lName}" # Returns Patricia Ong

# # print(format_name("PaTRicIA", "Ong"))
# formatted_Name = format_name("patriciA", "oNG")
# print(formatted_Name)


#
def format_name(fName, lName):
  # If fName and lName are empty.
  if fName == "" or lName == "":
    return "You didn't provide valid inputs." # Return a string.
  # Else, execute the rest of the function. 
  format_fName = fName.title()
  format_lName = lName.title()
  return f"Result: {format_fName} {format_lName}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
