numbers =[1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)  # [2, 3, 4]

name = "Angela"
letter_list = [letter for letter in name]
print(letter_list) # ['A', 'n', 'g', 'e', 'l', 'a']

range_list = [num * 3 for num  in range(1,5)]
print(range_list)

names = ["Alex","Beth","Carolina","Elanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)   # ['Alex', 'Beth']
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)   # ['CAROLINA', 'ELANOR', 'FREDDIE']

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)  # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

list_of_string = "9,0,45,67,89,34,23,28".split(",")
numbers = [int(x) for x in list_of_string]
result = [num for num in numbers if num%2 == 0]
print(result)  # [0, 34, 28]
