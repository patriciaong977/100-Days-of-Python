from turtle import Turtle, Screen
import random
# New turtle obj, inside turtle point variable.
turtle_Point = Turtle()

# Visual
turtle_Point.shape("turtle")
# turtle_Point.color("pale green")
# turtle_Point.pencolor("dark green")
turtle_Point.turtlesize(2,2,1) # (wide, len, outline)
turtle_Point.speed(1)

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

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon. (8 shapes)
  # Each shape is drawn with a random color.
  # Each sides are going to be 100 in terms of length.
  # 360 / num of sides.
colors = ["salmon", "dark orange", "RoyalBlue1","Chartreuse2",
          "goldenrod", "dark turquoise", "olive drab", "DeepSkyBlue2"]

for sides in range(3, 10):
    turtle_Point.color(random.choice(colors))   # Choose a random color from list.

    for i in range(sides):
        turtle_Point.forward(100)
        turtle_Point.right(360/sides)


# After execution of above.
screen = Screen()
screen.exitonclick()
