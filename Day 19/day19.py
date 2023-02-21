# Day 19: More Turtle Graphics, Event Listeners, State and Multiple Instances

## Higher Order Functions & Event Listeners ##

# Higher Order Function - function that can work with other functions.

'''
Event listener on Turtle Graphics
turtle.listen - allows the turtle screen to start listening for events that
the user might trigger.
'''

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Creating a binding function
def move_forwards():
  tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()


# #Functions as Inputs

# def function_a(something):
#   # Do this with something
#   # Then do this
#   # Finally do this

# def function_b():
#   # Do this

# Calculator is a higher order function because it is taking another function as an input,
#   and work with it in the body of the function.
# def calculator(n1, n2, func):
#   return func(n1, n2)

# result = calculator(2, 3, subtract)
