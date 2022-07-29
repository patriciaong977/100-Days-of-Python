# Dictionaries
  # Key and Value
  # Syntax: {Key:Value}
    # {
    #  "Bug": "An error in a program that prevents it from executing properly." ,
    #  "Function":"A piece of code that you can call over and over.",
    #  "Loop" : " The action of doing something repeatedly.",
    # }

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# How to retrieve an item from a dictionary? Call its key
# Syntax for calling a key: dictionary[key]
  # Note, use the correct data type when calling a key.
programming_dictionary["Bug"]
# print(programming_dictionary["Bug"]) # Should print the value of key.

# Adding new items to the dictionary.
programming_dictionary["Loop"] = "The action of doing something repeatedly."
# print(programming_dictionary) # Should print the dictionary with the Loop key and value.

# Creating an empty dictionary.
empty_dictionary = {}

# Wipe/Delete an existing dictionary.
# programming_dictionary = {}
# print(programming_dictionary) # Should print an empty dictionary.

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer. "
# print(programming_dictionary)  # Should print the new value 9.

# Loop through a dictionary.
for key in programming_dictionary:
  print(key) # Printed out just the keys.
  print(programming_dictionary[key]) # Printed out the values.


###################################################################################

# Nesting
  # A dictionary can contain another dictionary.
  # A dictionary can contain a list.

# syntax = {
#   "Key":[List],
#   "Key2":{Dict},
# }

# Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lyon", "Marseille"],
  "Germany": ["Berlin", "Munich", "Frankfurt"],
}

# Can have a list inside a list.
list_in_list = [["Paris", "Lyon", "Marseille"], ["Berlin", "Munich", "Frankfurt"]]

# Nest Dictionary inside a Dictionary
travel_log2 = {
  "France": {"cities_visited": ["Paris", "Lyon", "Marseille"], "total_visits": 12},    # Key: {Key:List, Key:Value}
  "Germany": {"cities_visited": ["Berlin", "Munich", "Frankfurt"], "total_visits": 5},
}

# Nesting Dictionary in a List. List of Dictionaries.
travel_log3 = [
  { # Dictionary 1 with 3 Key Value Pairs
    "country":"France",
    "cities_visited": ["Paris", "Lyon", "Marseille"],
    "total_visits": 12
  },
  { # Dictionary 2 with 3 Key Value Pairs
    "country":"Germany",
    "cities_visited": ["Berlin", "Munich", "Frankfurt"],
    "total_visits": 5
  },
]
