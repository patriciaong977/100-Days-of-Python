# Which line of code will change the starting_dictionary to the final_dictionary?
starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7  # Adding a new key and value to the dictionary.
final_dictionary = starting_dictionary # Changing the value of final_dictionary to the value of starting_dictionary.


# Which line of code will produce an error?
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
# dict["c"] = [1, 2, 3] # This will add a list to the value of the key "c".
# print(dict[1]) # This will produce an error.
# dict[1] = 4 # This will add 4 to the key 1.
# for key in dict:
  # dict[key] += 1 # This will add 1 to each value of the dictionary.


# Which line will print "Steak"?
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

# print(order["main"][2])
# print(order["dessert" - 1][2][0])
# print(order[main][2][0])
# print(order["main"][2][0]) # This will print "Steak".
