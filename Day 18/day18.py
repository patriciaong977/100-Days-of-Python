# Turtle Graphics - https://docs.python.org/3/library/turtle.html
# Turtle Colors - https://trinket.io/docs/colors
# Tuples
# Importing Modules

from turtle import Turtle, Screen

# New turtle object, inside timmy variable.
timmy_the_turtle = Turtle()

# Visual
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("hot pink")
timmy_the_turtle.pencolor("dark orchid")


# Tk color specification string.
  #https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
  # Tk = tkinter -- Python interface to Tcl/Tk --- https://docs.python.org/3/library/tkinter.html
    # One of the ways you can create a Graphical User Interface (GUI).
    # Color chart: http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html


# Movement
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)


# After execution of above.
screen = Screen()
screen.exitonclick()

