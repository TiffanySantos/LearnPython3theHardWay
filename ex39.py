
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}
#add more cities
cities = {
    "CA" : "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}
#print some cities
cities["NY"] = "New York"
cities["OR"] = "Portland"
#print some states
print('-' * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])
# do it by using the state then cities dict
print('-' * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Floridas's abbreviation is: ", states["Florida"])

print('-' * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])
#for every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated to {abbrev}")
#print every sity in the state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and the city has {cities[abbrev]}")

print('-' * 10)
state = states.get("Texas")
if not state:
    print("Sorry, no Texas")
#get a city with default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")


