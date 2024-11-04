import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

for_letters =int(input("How many letters would you like in your password/n"))

for_symbols = int(input("How many symbols would you like in your password/n"))

for_numbers =int(input("How many numbers would you like in your password/n"))

#Easy level i.e. 4 letters, 2 symbols and 2 numbers in an order.. 

#password = ""

#for char in range(0, for_letters):
#    password += random.choice(letters)

#for char in range(0, for_symbols):
#    password += random.choice(symbols)

#for char in range(0, for_numbers:)    
#    password += random.choice(numbers)

#print(password)



#Hard level i.e. items not in an randomized order. 

password_list = []

for char in range(0, for_letters):
    password_list.append( random.choice(letters))     

#We can use append for the same purpose of += which is also password_list = password_list + item in list     

for char in range(0, for_symbols):
    password_list.append( random.choice(symbols))
    
for char in range(0, for_numbers):
    password_list.append(random.choice(numbers))

print(password_list) 

random.shuffle(password_list) #Shuffles the items in a list.

print(password_list)  


#Conversion of list to string.
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

#for windows execution  
      
input('Press ENTER to exit!')