############## Turtle Example #######################
# Turtle graphics documentation: https://docs.python.org/3/library/turtle.html
# Turtle color names: https://cs111.wellesley.edu/labs/lab01/colors

# # Import module
# import turtle
# # Tap into the turtle module, and access the Turtle class.
# timmy = turtle.Turtle()


# Another way
# from turtle import Turtle, Screen
# timmy = Turtle()  # timmy is an object of the Turtle class.
# print(timmy)
# timmy.shape("turtle")      # Change shape of timmy.
# timmy.color("PaleGreen3")  # Change color of timmy.

# timmy.forward(100)  # Move turtle forward 100 paces.


# my_screen = Screen()  # Object = Blue print of Screen class.
# print(my_screen.canvheight)  # Access attributes of Screen.
# my_screen.exitonclick()  # Access methods of Screen.

################### End of Turtle Example ####################


####### Pretty Table ########

from prettytable import PrettyTable, MARKDOWN

# Create table
table = PrettyTable()

# Add data to table
table.field_names = ["Pokemon Name", "Type"]  # Add column names.
table.add_rows(                               # Add rows.
  [
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
  ]
)

# Customize table
table.set_style(MARKDOWN)  # Change style of table.

table.align = "l"  # Align table to left.
table.sortby = "Pokemon Name"  # Sort table by Pokemon Name.


print(table)
