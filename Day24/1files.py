file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    file.close()

with open("my_file.txt",mode="w") as file:
    file.write("new text")     # deletes everything and write new text

with open("my_file.txt",mode="a") as file:
    file.write("\nThis is Tom")     # append the new text

with open("new_file.txt",mode="w") as file:
    file.write("This is Sam")     # create the new file first and write in it
