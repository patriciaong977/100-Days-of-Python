# Python Functions
'''
# Syntax for creating a function:
def my_function(): # () - takes in an input/parameter.
  print("Hello")
  print("Bye")

my_function() # () - Calling the function.



# Indentation - Limit all lines to a maximum of 79 characters.
# For flowing long blocks of text with fewer structural restrictions #(docstrings or comments), the line length should be limited to 72 characters.


# While loops
# Syntax:
while something_is_true:
  # Do something repeatedly


# In reeborg's world:
def turn_right(): # Functions made.
  turn_left()
  turn_left()
  turn_left()

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

number_of_hurdles = 6 # Number of hurdles.

# Hurdle 1
while number_of_hurdles > 0: # While the number of hurdles is greater than 0.
  jump()  # Call the jump function.
  number_of_hurdles -= 1 # Decrease the number of hurdles by 1.

# Hurdle 2def turn_right():
# Use a while loop
while not at_goal(): # while at_goal != True:
    jump()


# When to use a for or a while loop?
# For
#   When you want to iterate over something and you need to do something with each iteration.
#   Using the range().
# While
#   When you don't care what number in a sequence you're on. You just want to do something with each iteration.
#   While loops will run until the condition is false.

# Hurdle 3:
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# Use a while loop
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


# Escaping the Maze in Reeborg's World.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear(): # It will seek a wall
    move()
turn_left() # Turn left when wall is found.

# While loop - Keep checking unless its at_Goal
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

'''
