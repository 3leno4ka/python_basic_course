import re
# from _random import randint
import random
phone_pattern = re.compile(r'(^\+[0-9]{12}$)')

name = input('Enter your name: ').capitalize()
surname = input('Enter your surname: ').capitalize()

full_name = f'{name} {surname}'[::-1]
print(full_name)

phone = ''
while True:
    phone = input("Enter number: ")
    if re.match(phone_pattern, phone):
        print('phone is correct')
    else:
        print('phone is not correct :(')
        continue
    break

has_333 = True if phone.count('3') == 3 else False
has_777 = True if phone.count('7') == 3 else False


if has_333 and has_777:
    print('Unbelievable!!')
elif has_333:
    print('You have a lucky number!')
elif has_777:
    print('You have a very lucky number!!')

random_digit = random.randint(0, 9)
print(f'random number is {random_digit}')
if phone.count(str(random_digit)) == 4:
    print('You have a randomly lucky number!!')
