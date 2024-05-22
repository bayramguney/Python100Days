print("Welcome to tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill?"))

bill_with_bill = tip / 100 * bill + bill

bill_per_person = bill_with_bill/people

# final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")
