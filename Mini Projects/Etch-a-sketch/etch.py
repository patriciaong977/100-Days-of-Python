from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()


# Functions to move
def move_forward():
  etch.forward(10)

def move_backward():
  etch.backward(10)

def move_left():
  m_left = etch.heading() + 10  # 10 degrees
  etch.setheading(m_left)

def move_right():
  m_right = etch.heading() - 10  # 10 degrees
  etch.setheading(m_right)

def clear():
  etch.clear()
  etch.penup()
  etch.home() # Move etch back to original coord.
  etch.pendown()


# Screen Output
screen.listen()

# Onkey, when key is pressed do the function.
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
