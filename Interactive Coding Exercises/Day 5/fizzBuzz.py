#Write your code below this row 👇
#Write your code below this row 👇

# Go through a list of 1 - 100 using the range().
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:  # If num is divisible by 3 and 5,
    print("FizzBuzz")
  elif num % 5 == 0:  # If num is divisible by 5,
    print("Buzz")
  elif num % 3 == 0:  # If num is divisible by 3,
    print("Fizz")
  else:
    print(num)

# Remember to do the AND operator first! 
