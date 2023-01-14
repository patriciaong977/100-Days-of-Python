# Python Tuples
'''
Syntax - my_tuple = (1,3,8)
Tuples are ordered.
Immutable - can't change.
Can convert tuple into a list by list(my_tuple)

https://www.w3schools.com/colors/colors_rgb.asp
'''
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgbTuple = (r,g,b)
    return rgbTuple

# colours = ["salmon", "dark orange", "RoyalBlue1", "Chartreuse2",
#           "goldenrod", "dark turquoise", "olive drab", "DeepSkyBlue2"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))
