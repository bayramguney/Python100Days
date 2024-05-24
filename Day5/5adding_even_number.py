target = int(input("Enter a number between 0 and 1000\n"))  # Enter a number between 0 and 1000
sum_even = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        sum_even += number

# for number in range(2, target + 1,2):
#     sum_even += number

print(sum_even)
