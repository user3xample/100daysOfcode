#! /usr/bin/env python3

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

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country_visited, times_visits, cities_visited):
    new_country = {}
    new_country ["country"] = country_visited
    new_country ["visits"] = times_visits
    new_country ["cities"] = cities_visited
    travel_log.append(new_country)

# When broken down like this it makes a bit more sense but im still struggling with visualising it all.






#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
