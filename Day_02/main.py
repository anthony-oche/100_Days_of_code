print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#get the percentage tip
tip_percentage = tip / 100
#multiply by the bill
bill_percentage = bill * tip_percentage
#add the bill percentage to the bill
total_bill = bill + bill_percentage
#divide the bill by the number of people playing
bill_per_person = round(total_bill / people, 2)

print(f"Each person should pay ${bill_per_person}")