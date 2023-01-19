### Extracting the rgb colors from an image ###
# Use colorgram.py
# import colorgram

# # Create list of colors
# rgb_list =[]
# # Extract the color from image.jp
# colors = colorgram.extract('image.jpg',30)

# # For each color in the list of colors extracted.
# for color in colors:
#     # Get each unique # of r, g, b.
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     # Create new list of color.
#     new_color = (r, g, b)
#     rgb_list.append(new_color)  #  Append the new_color to rgb_list.

# print(rgb_list)


## Paint Hirst Painting ##
# Create a painting with 10 x 10 spots.
# 20 size of the dots, spaced apart 50 paces.

import turtle as t
import random

# Turtle object
t_obj = t.Turtle()

t.colormode(255)  # For rgb colors.

# List of Random Colors
rgb_list = [ (202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

# Turtle Movement and Appearance
t_obj.hideturtle()  # Hide the turtle.
t_obj.speed("fastest")  # Turtle Speed
t_obj.penup() # Pen is not writing

# Set turtle's position from middle to the bottom right.
num_x = -200
num_y = -200
t_obj.setposition(num_x, num_y)
num_dots = 100

#
for dots in range(1, num_dots + 1):
  t_obj.dot(20, random.choice(rgb_list)) # Size, color of dot.
  #t_obj.penup()
  t_obj.forward(50)

  if dots % 10 == 0:
      num_y += 50
      t_obj.setposition(num_x, num_y)

# Display Screen, Exit screen onClick.
screen = t.Screen()
screen.exitonclick()
