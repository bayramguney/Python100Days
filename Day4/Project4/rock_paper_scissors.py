import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n "))

choices = ["Rock","Paper","Scissors"]
choices_symbol = [rock,paper,scissors]

computer_choice = random.randint(0,2)
if choice >= 3 or choice < 0:
    print("It's an invalid entry.You lose!")
else:
    print(f"Your choice is {choices[choice]}\n {choices_symbol[choice]} ")
    print(f"Computer choice is {choices[computer_choice]}\n {choices_symbol[computer_choice]} ")

    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 2 and computer_choice == 0:
        print("You lose")
    elif computer_choice > choice:
        print("You lose")
    elif choice > computer_choice:
        print("You win")
    elif computer_choice == choice:
        print("It's  a draw")
    elif choice > 3 or choice < 0:
        print("It's an invalid entry.You lose!")








