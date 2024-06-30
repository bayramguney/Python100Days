# File not found
# with open("a_file") as file:
#     file.read()

# Key error
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existing_key"]

# index error
# fruit_list = ["apple","cherry"]
# fruit = fruit_list[2]

# Type error
# text = "abc"
# print(text + 1)

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file closed")

