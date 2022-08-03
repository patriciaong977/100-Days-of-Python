# Question 1: Without running the code below, what do you think will be printed in the console?

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

print(add(2, multiply(5, divide(8, 4))))
  # Divide (8, 4) = 2
    # Multiply (5, 2) = 10
      # Add (2, 10) = 12

# 10
# 12.0 -- Correct
# 0.21
# 14


# Question 2: What would you predict to be the result of running the following code?

def outer_function(a, b): # 5, 10
    def inner_function(c, d): # 5, 10
        return c + d  # 5 + 10 = 15
    return inner_function(a, b)

result = outer_function(5, 10)
print(result)

# SyntaxError
# 15 -- Correct
# 10
# (5, 10)

# Question 3: What will be printed in the console after running the following code?

def my_function(a):
  if a < 40:  # 20 < 40
    return  # Return None. 
    print("Terrible")
  if a < 80:
    return "Pass"
  else:
    return "Great"
print(my_function(25))

# NameError
# SyntaxError
# None --- Correct
# "Pass"
# "Great"
