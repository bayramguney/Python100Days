height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should be over 3 meter")
bmi = weight/height ** 2
print(bmi)