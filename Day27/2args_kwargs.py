def add(*args):
    print(args[2])
    total = 0
    for n in args:
        total += n
    return total

print(add(3,5,7))
print("@@ KWARGS @@")

def calculate(n,**kwargs):
    print(kwargs)  # {'add': 3, 'multiply': 5}
    # for key,value in kwargs.items():
    #     print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(model="GTI",color="Red")
print(my_car.model,my_car.color)