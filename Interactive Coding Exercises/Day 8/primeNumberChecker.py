# Write your code below this line 👇

# Need to use modulus to get the remainder of the division: https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python

# Write a function that checks if a number is prime.
def prime_checker(number):
    is_prime = True  # Set is_prime to True

    # Prime numbers are numbers that can only be cleanly divided by themselves and 1.
    # i - number to check if it is divisible by any number between 2 and number.
    for i in range(2, number):
        if number % i == 0:  # Check the remainder. If it is 0, then it is not a prime number.
            is_prime = False

    # Print the result.
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
