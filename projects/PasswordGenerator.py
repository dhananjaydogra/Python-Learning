#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwordlist = []

# for letter in range(0,nr_letters):
#     passwordlist.append(letters[random.randint(0,len(letters)-1)])

# for symbol in range(0,nr_symbols):
#     passwordlist.append(symbols[random.randint(0,len(symbols)-1)])

# for number in range(0, nr_numbers):
#     passwordlist.append(numbers[random.randint(0, len(numbers) - 1)])

##Easier Alternative
for char in range(0,nr_letters):
    passwordlist+=random.choice(letters)

for char in range(0,nr_symbols):
    passwordlist+=random.choice(symbols)

for char in range(0,nr_numbers):
    passwordlist+=random.choice(numbers)

print(passwordlist)
random.shuffle(passwordlist)
print(passwordlist)
password=""

for passletter in passwordlist:
    password=password + passletter
    
print(f"Your password is : {password}")