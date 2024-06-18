# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)     # list does not have dice_imgs[6]    correction ( 0, 5)
print(dice_imgs[dice_num])