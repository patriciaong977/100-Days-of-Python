from turtle import Turtle, Screen
import random
import turtle
# New turtle obj, inside turtle point variable.
turtle_Point = Turtle()

# Visual
turtle_Point.shape("turtle")
# turtle_Point.color("pale green")
# turtle_Point.pencolor("dark green")
turtle_Point.turtlesize(1.5,1.5,1.5) # (wide, len, outline)
# turtle_Point.speed(1)

# Movement
# # Draw a Square
# for i in range(4):
#     turtle_Point.forward(100)
#     turtle_Point.right(90)

# # Draw a Dashed Line
#   # Draw a lined for 10 paces and then a gap of 10 paces, then solid line for 10 paces.
#   # Do this 15 times.
#   # Length of line doesn't matter, length of each sections doesn't matter.
# for i in range(15):
#     turtle_Point.pendown()  # Not drawing when moving.
#     turtle_Point.forward(10)
#     turtle_Point.penup()  # Drawing when moving.
#     turtle_Point.forward(10)

# # Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon. (8 shapes)
#   # Each shape is drawn with a random color. https://trinket.io/docs/colors
#   # Each sides are going to be 100 in terms of length.
#   # 360 / num of sides.
# colors = ["salmon", "dark orange", "RoyalBlue1","Chartreuse2",
#           "goldenrod", "dark turquoise", "olive drab", "DeepSkyBlue2"]

# for sides in range(3, 11): # 11 - stop number is included. Will stop at 10.
#     turtle_Point.color(random.choice(colors))   # Choose a random color from list.

#     for _ in range(sides):  #  360 / 3 = 120, 360 / 4 = 90 ...
#         turtle_Point.forward(100)
#         turtle_Point.right(360 / sides)

# # Draw a Random Walk.
#   # Turtle making a random walk (north, south, east, west).\
#   # Increase thickness.
#   # Increase speed.
#   #

# colors = ["salmon", "dark orange", "RoyalBlue1", "Chartreuse2",
#           "goldenrod", "dark turquoise", "olive drab", "DeepSkyBlue2"]

# # East = 0, North = 90, West = 180, South = 270
# direction = [0, 90, 180, 270]

# turtle_Point.speed(10)
# turtle_Point.pensize(8)

# # Movement
# for _ in range(100):
#     turtle_Point.color(random.choice(colors)) # Change colors

#     # Set orientation of the turtle. (Use angles)
#     turtle_Point.setheading(random.choice(direction))
#     turtle_Point.forward(20)


# Make a Spirograph
  # Get the turtle to draw a number of circles each with a radius of a 100 in distance.
  # Use random colors and documentation

turtle.colormode(255)

# Random Color function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_tuple = (r,g,b)
    return rgb_tuple

# Turtle Looks
# turtle_Point.pensize(15)
turtle_Point.speed("fastest")

def spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        turtle_Point.color(random_color())
        turtle_Point.circle(100)
        turtle_Point.setheading(turtle_Point.heading() + gap_size)

spirograph(5) # Call the gap

# After execution of above.
screen = Screen()
screen.exitonclick()
