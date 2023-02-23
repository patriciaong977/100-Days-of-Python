from turtle import Turtle, Screen
import random

is_race_on = False
# Set up the screen size
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user what color.
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_input)
turtle_color = ["red", "orange", "yellow","green","blue", "purple"]
y_turtle = [-70, -40, -10, 20, 50, 80]
list_turtle = []

# Initialize Turtles
for i in range(0,6):  # For every i from 0 - 6 (0,1,2,3,4,5)
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(turtle_color[i]) # Set a color for each index from turtle_color.
  new_turtle.penup()
  new_turtle.goto(x=-230, y=y_turtle[i]) # Set each turtle into x and y.
  list_turtle.append(new_turtle)

# If user_bet exists, turn on race.
if user_input:  # Race doesn't start til' user bets.
  is_race_on = True

# Start the race, move the turtles.
while is_race_on:
  for turtle in list_turtle:

    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_input:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")

    r_distance = random.randint(0, 10)
    turtle.forward(r_distance)

screen.exitonclick()
