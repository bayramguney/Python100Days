# There is no block scope

game_level = 3
def create_enemy():
    enemies = ["Skeleton","zombie","Alien"]
    if game_level <5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()