#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# 1st way
# for letter in range(0, nr_letters):
#     print(random.choice(letters),end ="")
# for symbol in range(0, nr_symbols):
#     print(random.choice(symbols),end ="")
# for number in range(0, nr_numbers):
#     print(random.choice(numbers),end ="")

# 2nd way
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))
random.shuffle(password)

final_password = ""
for char in password:
    final_password += char
print(final_password)