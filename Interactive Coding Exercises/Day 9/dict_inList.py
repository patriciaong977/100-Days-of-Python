travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, count_visits, name_cities): # The data inputs.
  new_country = {} # Empty dictionary to add to travel_log list.

  new_country["country"] = country_name # Add the key "country" and value of country_name.
  new_country["visits"] = count_visits  # Add the key "visits" and value of count_visits.
  new_country["cities"] = name_cities   # Add the key "cities" and value of name_cities.

  # Add the new country dictionary to the travel_log list.
  travel_log.append(new_country) # Append - Add to the end of the list.


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
