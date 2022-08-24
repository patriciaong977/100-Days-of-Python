# # Scope

# enemies = 1 # Global Variable

# # Inside the function, enemies is 2.
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# # Outside the function, enemies is 1
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # Local Scope
# def game():
#   def drink_potion():
#     potion_strength = 2 # Local Variable
#     print(potion_strength)

#   drink_potion()

# print(potion_strength) # potion_strength is not defined outside of the function.

# # Namespace - Global and Local


# # Does python have block scope? No.
# if 3 > 2:
#   a_var = 10 # Still global.

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#   new_enemy = enemies[0]

# print(new_enemy)


# # Modify a Global Variable (Avoid modifying global variables)
# enemies = 1

# def increase_enemies():
#   # global enemies # Call the variable outside the function. (Global variable)
#   # enemies += 1
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants
# Global constants should be in uppercase and separated by underscores.
PI = 3.14159265359
URL = "https://www.python.org"
TWITTER_URL = "https://twitter.com/python"
