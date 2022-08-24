# Question 1:

# What will be printed in the console when the following code is run?

# DO NOT run the code, just pretend to be a computer.

#    def a_function(a_parameter):
#         a_variable = 15
#         return a_parameter

#     a_function(10)
#     print(a_variable)


# NameError -- Correct: Its trying to print a var that is local to a_function and is only available inside the function.
# 10
# 15
# SyntaxError


# Question 2:

# What will be printed in the console when the code is run?

# DO NOT run the code, just pretend to be a computer.

#   i = 50

#    def foo():
#         i = 100
#         return i

#     foo()
#     print(i)


# 100
# 50 -- Correct: The print statement is outside of the function foo(). So it can't access the local variable i. Only sees global i, which is 100.
# 150
# NameError

# Question 3:

# What will be printed in the console when the following code is run?

# DO NOT run the code, just pretend to be a computer.

#    def bar():
#         my_variable = 9

#         if 16 > 9:
#           my_variable = 16

#         print(my_variable)

#     bar()

# 9
# 16 -- Correct: Python has no block scope. Inside a if/else/for/while code block is the same as outside it. 
# NameError
# Nothing will be printed.
