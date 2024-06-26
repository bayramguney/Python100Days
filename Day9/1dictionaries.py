programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    123: "this is a number"
}

print(programming_dictionary["Bug"])
print(programming_dictionary[123])

# adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and again"
print(programming_dictionary)

# create a new empty dict
empty_dictionary = {}

# # wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dict
programming_dictionary["Bug"] = "this is new description"
print(programming_dictionary)

#Loop through a dictonary
for key in programming_dictionary:
    print(key)                    # gives just keys
    print(programming_dictionary[key])   # gives just values
