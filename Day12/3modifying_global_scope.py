enemies = 1
def increase_enemies():
    # enemies += 1
    print(f"Enemies inside function : {enemies}")
    return enemies +1

enemies = increase_enemies()
print(f"Enemies outside function  : {enemies}")