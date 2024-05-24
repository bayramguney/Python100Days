import random

chance = random.randint(0,1)
print(chance)

if chance == 0:
    print("Tails")
else:
    print("Heads")