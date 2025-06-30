print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill= 0
#check for the size of pizza they want and add it to their bill
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25

#check if their want pepperoni, size of pizza has a type of pepperoni
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
#check if their want extra cheese and get the final bill
if extra_cheese == "y":
    bill += 1
else:
    pass
print(f"Your final bill is: ${bill}.")