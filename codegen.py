#Goal is to create password

import random 

#Program intro
print("Welcome to our password gen app")

#Set password length
pw_length = int(input("Enter length of password"))

# Password criteria
lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

pw_symbols = lowercase.copy()

has_upper = input("Include uppercase characters? (y/n): ")
if has_upper == 'Y' or has_upper == 'y':
    pw_symbols.extend(uppercase)

has_special = input("Include special characters? (y/n): ")
if has_special == 'Y' or has_special == 'y':
    pw_symbols.extend(special)
    
has_digits = input("Include digits characters? (y/n): ")
if has_digits == 'Y' or has_digits == 'y':
    pw_symbols.extend(digits)
    
new_pwd = ""

while len(new_pwd) != pw_length:
    random_symbol = chr(random.choice(pw_symbols))
    new_pwd = new_pwd + random_symbol

print(f"{new_pwd} has been generated")