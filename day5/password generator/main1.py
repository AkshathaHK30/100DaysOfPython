#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_str = ''.join(random.choice(letters) for i in range(nr_letters))
# print(letter_str)
number_str = ''.join(random.choice(numbers) for i in range(nr_numbers))
# print(number_str)
symbol_str = ''.join(random.choice(symbols) for i in range(nr_symbols))
# print(symbol_str)
random_password = letter_str+number_str+symbol_str
shuffled = ''.join(random.sample(random_password, len(random_password)))
'''
Shuffle the letters:
random.sample(word, len(word)) creates a new list with all the letters from the word, but in a random order.
''.join(...) joins the letters in the shuffled list back into a string.
'''
# random.shuffle(random_password)
print(f"Your Password is {shuffled}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
