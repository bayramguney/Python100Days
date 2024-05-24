print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")  # What is your name?
name2 = input("What is their name?")  # What is their name?

combined_name = (name1 + name2).lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

count1 = t+r+u+e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

count2 = l+o+v+e

love_score = int(str(count1)+str(count2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")






