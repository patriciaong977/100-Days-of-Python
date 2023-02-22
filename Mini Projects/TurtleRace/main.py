from turtle import Turtle, Screen

# Set up the screen size
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user what color.
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_input)

tim = Turtle()
tim.goto(x=230, y=-100)

screen.exitonclick()
