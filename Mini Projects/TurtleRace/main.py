from turtle import Turtle, Screen

# Set up the screen size
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user what color.
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_input)
turtle_color = ["red", "orange", "yellow","green","blue", "purple"]
y_turtle = [-70, -40, -10, 20, 50, 80]

# Initialize Turtles
for i in range(0,6):  # For every i from 0 - 6 (0,1,2,3,4,5)
  tim = Turtle(shape="turtle")
  tim.color(turtle_color[i]) # Set a color for each index from turtle_color.
  tim.penup()
  tim.goto(x=-230, y=y_turtle[i]) # Set each turtle into x and y.

# Start moving turtles

screen.exitonclick()
