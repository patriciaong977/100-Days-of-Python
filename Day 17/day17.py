# Creating Classes
'''
Syntax for classes
class <classname>:


Creating User Object

classVariable = className()
# user_1 = User()

Pascal Case = Name of class should have the first letter of every word capitalized.
EX: PascalCase
  - used for class names

camel Case = every subsequent word has its first letter capitalized.
Ex. camelCase

snake case = underscore on every space.
Ex. snake_case
  - used for everything else


Constructors - initializing.
Use a special function called init.

def __init__(self):
    # initialize attributes

'''

# Simple Class
class User:
    # Empty Class
    # pass  # So that the indentation error disappears since class is empty atm.

    # Showing constructor
    def __init__(self, user_id, username): # When a User() is being created, it calls this.
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Can create methods.
    # Needs to have self param, always.
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Create an attribute of that class.
  # Attribute - variable associated with an object.
# user_1.id = "001"
user_1 = User("001", "isha")
# user_1.username = "isha"

user_2 = User("002", "Poot")

user_1.follow(user_2)
print(f"{user_1.username} has {user_1.followers} followers")
print(f"{user_1.username} is following {user_1.following}")

print(f"{user_2.username} has {user_2.followers} followers")
print(f"{user_2.username} is following {user_2.following}")

# When a function is attached to an object its called a method.
