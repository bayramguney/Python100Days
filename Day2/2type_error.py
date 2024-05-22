# len(1234)   type error
num_char = len(input("What is your name"))
# print("Your name has "+num_char+" characters")  type error
new_num_char = str(num_char)  # type conversion
print("Your name has " + new_num_char + " characters")

print(type(num_char))

a = 123
type(str(a))  # String
type(float(a))  # float

print(70 + float(100.2))  # 170.2
