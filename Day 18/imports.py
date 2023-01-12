## Importing Modules ##
'''
Use if you're using once or twice.
import turtle
import = keyword
turtle = module name
'''

# import turtle
# tim = turtle.Turtle()

'''
Use this if you're using something from a module > 3 times.
from turtle import Turtle
from = keyword
turtle = module name
import = keyword
Turtle = thing in Module
'''

# from turtle import Turtle
# tom = Turtle()
# terry = Turtle()

'''
Try to avoid this:
from turtle import *
from = keyword
turtle = module name
* = everything
'''

# from turtle import *
# from random import *

## Aliasing Modules ##
'''
import turtle as t
import = keyword
turtle = module name
as = keyword
t = alias name
'''

# import turtle as t
# tim = t.Turtle()


## Installing Modules ##
'''
Importing heroes module.
Turtle is a module that's package with the Python standard library.
Python packages have the heroes module which you need to install into the project.
There are packages that need to be installed. 
'''
import heroes # pip install heroes
print(heroes.gen())
