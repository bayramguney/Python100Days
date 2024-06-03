enemies = 1
def increase_enemies():
    enemies = 2
    print(f"Enemies inside function : {enemies}")

increase_enemies()
print(f"Enemies outside function  : {enemies}")

#local scope
def drink_potion():
    poition_strength = 2
    print(poition_strength)

drink_potion()
# print(poition_strength)    error

# global scope
player_heath = 10   # global 
def drink_potion():
    poition_strength = 2
    print(player_heath)

drink_potion()