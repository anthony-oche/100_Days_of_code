import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_alphabets = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#looping through the alphabet and randomly selecting letters in range of specified number
for letter in range(nr_alphabets):
    random_letters = random.choice(alphabets)
    password.append(random_letters)

#looping through the symbols and randomly selecting signs in range of specified number
for sym in range(nr_symbols):
    random_symbols = random.choice(symbols)
    password.append(random_symbols)

#looping through the numbers and randomly selecting number in range of specified number
for num in range(nr_numbers):
    random_numbers = random.choice(numbers)
    password.append(random_numbers)

#password list
print(password)
#shuffling the password list
random.shuffle(password)

new_password = ""

#creating our shuffled password into a string
for pwd in password:
    new_password += pwd

#Final password in a string
print(f"Your new password is: {new_password}")





