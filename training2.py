# list seems like an array
[1, 2, 3]
["jane", "john", "alex"]
names = ["jane", "john", "alex"]

# how to get the first name in names?
print(names[0])

names[0] = "Jen"

print(names[0])

# this should show "true" since jen is in the list of names
print("Jen" in names)

# only letters and underscores for this title
# this is called a dictionary, but it seems like object
name_to_cookies = {"jane": 3, "john": 2}
print(name_to_cookies["jane"])

name_to_cookies["jane"] = 10


numbers = [4, 5, 2]

numbers2 = [4, 2, 7]

strings = ["a", "b", "c"]

booleans = [True]

numbers[0]

strings[2]

# remember dictionary is {} list is [] just object and array really
name_to_hungry = {"Jack": False, "Jane": True, "Alex": True}

name_to_burgers = {"Emily": 1, "Jenny": 2, "Neel": 3}

names_to_names = {"Jack": "Emily", "Jen": "Neel", "Alex": "Bob"}

age_to_name = {14: "Bob", 15: "Alex", 20: "Jenny"}

# this should equal False
name_to_hungry["Jack"]

# this should be 3
name_to_burgers["Neel"]

list_of_dictionaries = [{"a": 1}, {"b": 2}]

strings_to_lists = {"Jack": [1, 2, 3]}